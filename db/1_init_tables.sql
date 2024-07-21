-- create table "departments" (
--   "id" serial primary key,
--   "department_name" varchar(255) null,
--   "access_level" smallint not null, -- low priority
--   "created_at" timestamp not null default NOW(),
--   "updated_at" timestamp not null default NOW()
-- );

-- create table "users" (
--   "id" serial primary key,
--   "full_name" varchar(255) not null,
--   "email" varchar(255) not null,
--   "password" varchar(255) not null,
--   "department_id" INTEGER not null DEFAULT 0,
--   "access_level" smallint not null DEFAULT 0, -- high priority
--   "created_at" timestamp not null default NOW(),
--   "updated_at" timestamp not null default NOW(),
--   FOREIGN KEY (department_id) REFERENCES departments (id) ON DELETE CASCADE,
--   UNIQUE(email)
-- );

create table "tickets_simple" (
    "id" serial primary key,
    "uuid" uuid not null,
    "user_id" INTEGER not null,
    "email" varchar(255) not null,
    "district" varchar(50) not null,
    "priority" smallint not null,
    "text" varchar(1024) not null
);