create table "access_levels" (
    "id" serial primary key,
    "level_name" varchar(50) not null,
    "can_create_reports" BOOLEAN DEFAULT FALSE,
    "can_read_reports" BOOLEAN DEFAULT FALSE,
    "can_answer_reports" BOOLEAN DEFAULT FALSE
);
INSERT INTO access_levels (level_name) VALUES ('Без доступа');
INSERT INTO access_levels (level_name, can_create_reports) VALUES ('Только отправка', True);
INSERT INTO access_levels (level_name, can_create_reports, can_read_reports) VALUES ('Отправка и просмотр', True, True);


create table "departments" (
  "id" serial primary key,
  "department_name" varchar(255) not null,
  "access_level" smallint not null DEFAULT 1,
  "created_at" timestamp not null default NOW(),
  "updated_at" timestamp not null default NOW(),
  FOREIGN KEY (access_level) REFERENCES access_levels (id) ON DELETE CASCADE
);
INSERT INTO departments (department_name, access_level) VALUES ('Гости', 1), ('Сотрудники', 2), ('Администраторы', 3);


create table "users" (
  "id" serial primary key,
  "employee_id" smallint not null,
  "first_name" varchar(50) not null, -- имя
  "middle_name" varchar(50), -- отчество
  "last_name" varchar(50) not null, -- фамилия
  "email" varchar(255) not null,
  "password" varchar(32) not null, --md5
  "department_id" INTEGER not null DEFAULT 1,
  "created_at" timestamp not null default NOW(),
  "updated_at" timestamp not null default NOW(),
  FOREIGN KEY (department_id) REFERENCES departments (id) ON DELETE CASCADE,
  UNIQUE(email),
  UNIQUE(employee_id)
);


create table "priority_list" (
    "id" serial primary key,
    "priority_name" varchar(20) not null
);
INSERT INTO priority_list (priority_name) VALUES ('Низкий'), ('Обычный'), ('Высокий');


create table "problems_list" (
    "id" serial primary key,
    "problem_name" varchar(20) not null
);
INSERT INTO problems_list (problem_name) VALUES ('Общее'), ('Электроника');



create table "tickets" (
    "id" serial primary key,
    "uuid" uuid not null,
    "reporter_id" INTEGER not null,
    "priority_id" INTEGER not null DEFAULT 2,
    "problem_id" INTEGER not null DEFAULT 1,
    "text" varchar(1024) not null,
    "created_at" timestamp not null default NOW(),
    FOREIGN KEY (reporter_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (priority_id) REFERENCES priority_list (id) ON DELETE CASCADE,
    FOREIGN KEY (problem_id) REFERENCES problems_list (id) ON DELETE CASCADE
);


create table if not exists "tickets_simple" (
    "id" serial primary key,
    "uuid" uuid not null,
    "user_id" INTEGER not null,
    "email" varchar(255) not null,
    "district" varchar(50) not null,
    "priority" varchar(20) not null,
    "text" varchar(1024) not null,
    "created_at" timestamp not null default NOW()
);