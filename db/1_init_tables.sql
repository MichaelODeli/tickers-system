create table
  "access_levels" (
    "id" serial primary key,
    "level_name" varchar(50) not null,
    "can_create_reports" BOOLEAN DEFAULT FALSE,
    "can_read_reports" BOOLEAN DEFAULT FALSE,
    "can_answer_reports" BOOLEAN DEFAULT FALSE,
    "can_view_analytics_data" BOOLEAN DEFAULT FALSE,
    "admin_access" BOOLEAN DEFAULT FALSE,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW()
  );


create table
  "departments" (
    "id" serial primary key,
    "department_name" varchar(255) not null,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW()
  );


create table
  "positions" (
    "id" serial primary key,
    "position_name" varchar(255) not null,
    "department_id" INTEGER not null,
    "access_level" smallint not null DEFAULT 2,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW(),
    FOREIGN KEY (department_id) REFERENCES departments (id) ON DELETE CASCADE,
    FOREIGN KEY (access_level) REFERENCES access_levels (id) ON DELETE CASCADE
  );


create table
  "users" (
    "id" serial primary key,
    "employee_id" integer not null,
    "first_name" varchar(50) not null,
    "middle_name" varchar(50),
    "last_name" varchar(50) not null,
    "username" varchar(70) not null,
    "email" varchar(150) not null,
    "password" varchar(64) not null,
    "position_id" INTEGER not null,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW(),
    FOREIGN KEY (position_id) REFERENCES positions (id) ON DELETE CASCADE,
    UNIQUE(email),
    UNIQUE(username),
    UNIQUE(employee_id)
  );


create table
  "priority_list" (
    "id" serial primary key,
    "priority_name" varchar(20) not null,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW()
  );


create table
  "problems_list" (
    "id" serial primary key,
    "problem_name" varchar(50) not null,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW()
  );

create table
  "steps_list" (
    "id" serial primary key,
    "step_name" varchar(50) not null,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW()
);

create table
  "status_list" (
    "id" serial primary key,
    "status_name" varchar(50) not null,
    "step_id" smallint not null,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW(),
    FOREIGN KEY (step_id) REFERENCES steps_list (id) ON DELETE CASCADE
  );


create table
  "tickets" (
    "uuid" uuid not null primary key,
    "reporter_id" INTEGER not null,
    "priority_id" INTEGER not null DEFAULT 2,
    "problem_id" INTEGER not null DEFAULT 1,
    "status_id" smallint not null DEFAULT 0,
    -- "reviewer_id" smallint,
    "text" varchar(1024) not null,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW(),
    FOREIGN KEY (reporter_id) REFERENCES users (id) ON DELETE CASCADE,
    -- FOREIGN KEY (reviewer_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (priority_id) REFERENCES priority_list (id) ON DELETE CASCADE,
    FOREIGN KEY (problem_id) REFERENCES problems_list (id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES status_list (id) ON DELETE CASCADE
  );

create table "tickets_review" (
  "uuid" uuid not null,
  "reviewer_id" INTEGER,
  "assigned_status" INTEGER not null,
  "text" varchar(1024),
  "created_at" timestamp not null default NOW(),
  "updated_at" timestamp not null default NOW(),
  FOREIGN KEY (reviewer_id) REFERENCES users (id) ON DELETE CASCADE,
  FOREIGN KEY (previous_status) REFERENCES status_list (id) ON DELETE CASCADE,
  FOREIGN KEY (assigned_status) REFERENCES status_list (id) ON DELETE CASCADE,
  FOREIGN KEY (uuid) REFERENCES tickets (uuid) ON DELETE CASCADE
);

-- реакция на вставку колонок
-- после вставки нового тикета - его номер дублируется в таблицу tickets_review

CREATE OR REPLACE FUNCTION trigger_insert_ticket() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO tickets_review (uuid, assigned_status) VALUES (NEW.uuid, 0);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER insert_ticket_trigger
AFTER INSERT ON "tickets"
FOR EACH ROW EXECUTE PROCEDURE trigger_insert_ticket();

-- реакция на обновление статуса тикета
-- после обновления статуса - его актуальный статус помещается в основную таблицу с тикетами

CREATE OR REPLACE FUNCTION trigger_update_ticket_status() RETURNS TRIGGER AS $$
DECLARE
    latest_status INT;
BEGIN
    SELECT assigned_status INTO latest_status FROM tickets_review WHERE uuid = NEW.uuid ORDER BY created_at DESC LIMIT 1;
    IF FOUND THEN
        UPDATE tickets SET status_id = latest_status, update_at = NOW() WHERE uuid = NEW.uuid;
    END IF;
    RETURN NULL; -- сигнализирует о том, что триггер не влияет на изменения
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_status_trigger
AFTER INSERT OR UPDATE OF assigned_status ON tickets_review
FOR EACH ROW EXECUTE PROCEDURE trigger_update_status();