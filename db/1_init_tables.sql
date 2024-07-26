create table
  "access_levels" (
    "id" serial primary key,
    "level_name" varchar(50) not null,
    "can_create_reports" BOOLEAN DEFAULT FALSE,
    "can_read_reports" BOOLEAN DEFAULT FALSE,
    "can_answer_reports" BOOLEAN DEFAULT FALSE,
    "can_view_analytics_data" BOOLEAN DEFAULT FALSE,
    "admin_access" BOOLEAN DEFAULT FALSE
  );


create table
  "departments" (
    "id" serial primary key,
    "department_name" varchar(255) not null,
    -- "access_level" smallint not null DEFAULT 2,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW() -- FOREIGN KEY (access_level) REFERENCES access_levels (id) ON DELETE CASCADE
  );


create table
  "positions" (
    "id" serial primary key,
    "position_name" varchar(255) not null,
    "department_id" INTEGER not null,
    "access_level" smallint not null DEFAULT 2,
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
    "username" varchar(255) not null,
    "email" varchar(255) not null,
    "password" varchar(32) not null,
    "position_id" INTEGER not null,
    -- "department_id" INTEGER not null DEFAULT 1,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW(),
    -- FOREIGN KEY (department_id) REFERENCES departments (id) ON DELETE CASCADE,
    FOREIGN KEY (position_id) REFERENCES positions (id) ON DELETE CASCADE,
    UNIQUE(email),
    UNIQUE(username),
    UNIQUE(employee_id)
  );


create table
  "priority_list" (
    "id" serial primary key,
    "priority_name" varchar(20) not null
  );


create table
  "problems_list" (
    "id" serial primary key,
    "problem_name" varchar(50) not null
  );


create table
  "tickets" (
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


create table
  if not exists "tickets_simple" (
    "id" serial primary key,
    "uuid" uuid not null,
    "user_id" INTEGER not null,
    "email" varchar(255) not null,
    "district" varchar(50) not null,
    "priority" varchar(20) not null,
    "text" varchar(1024) not null,
    "created_at" timestamp not null default NOW()
  );