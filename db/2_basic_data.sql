-- 1
INSERT INTO
  access_levels (id, level_name)
VALUES
  (1, 'Без доступа');

-- 2
INSERT INTO
  access_levels (id, level_name, can_create_reports)
VALUES
  (2, 'Только отправка', True);

-- 3
INSERT INTO
  access_levels (id, level_name, can_create_reports, can_read_reports)
VALUES
  (3, 'Отправка и просмотр', True, True);

-- 4
INSERT INTO
  access_levels (
    id, 
    level_name,
    can_create_reports,
    can_read_reports,
    can_answer_reports
  )
VALUES
  (4, 'Отправка, просмотр и ответ', True, True, True);

-- 5
INSERT INTO
  access_levels (
    id, 
    level_name,
    can_create_reports,
    can_read_reports,
    can_view_analytics_data
  )
VALUES
  (5, 'Отправка, просмотр и аналитика', True, True, True);


INSERT INTO
  access_levels (
    id, 
    level_name,
    can_create_reports,
    can_read_reports,
    can_answer_reports,
    can_view_analytics_data,
    admin_access
  )
VALUES
  (6, 'Администрирование', True, True, True, True, True);



INSERT INTO
  priority_list (id, priority_name)
VALUES
  (0, 'Низкий'),
  (1, 'Обычный'),
  (2, 'Высокий');


INSERT INTO
  problems_list (id, problem_name)
VALUES
  (1, 'Общее'),
  (2, 'Электроника'),
  (3, 'Документооборот'),
  (4, 'Информ. система'),
  (5, 'Почта'),
  (6, '1С');

INSERT INTO
  steps_list (id, step_name)
VALUES
  (0, 'Открыт'),
  (1, 'В работе'),
  (2, 'Закрыт');

INSERT INTO
  status_list (id, status_name, step_id)
VALUES
  (0, 'Создан', 0),
  (1, 'На рассмотрении', 1),
  (2, 'В работе', 1),
  (3, 'Отложен', 1),
  (4, 'Передан в другой отдел', 1),
  (5, 'Завершен', 2);