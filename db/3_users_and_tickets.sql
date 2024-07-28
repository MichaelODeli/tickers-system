-- Случайные данные. Любые совпадения с реальными данными случайны.

INSERT INTO
  departments (id, department_name)
VALUES
  (0, 'Гости'),
  (1, 'Отдел технической поддержки'),
  (2, 'Отдел охраны труда'),
  (3, 'Отдел информатизации'),
  (4, 'Отдел закупок'),
  (5, 'Бухгалтерия');


INSERT INTO
  positions (id, position_name, department_id, access_level)
VALUES
  (0, 'Администратор сервиса поддержки', 1, 6),
  (1, 'Аналитик', 1, 5),
  (2, 'Специалист технической поддержки', 1, 4),
  (3, 'Младший сотрудник', 2, 2),
  (4, 'Младший сотрудник', 3, 2),
  (5, 'Младший сотрудник', 4, 2),
  (6, 'Младший сотрудник', 5, 2),
  (7, 'Гость', 0, 1);


INSERT INTO users (id, employee_id, first_name, middle_name, last_name, username, email, password, position_id) VALUES 
	(1, 75806698, 'Евгений', 'Олегович', 'Иванов', 'test', 'admin@internal.portal', encode(sha256('test'::bytea), 'hex'), 0),
	(2, 58971200, 'Григорий', 'Евгеньевич', 'Тротиллов', 'tost', 'analitic@internal.portal', encode(sha256('tost'::bytea), 'hex'), 1),
	(3, 58971201, 'Леонид', 'Ролеплеевич', 'Пахомов', 'tist', 'tech_support@internal.portal', encode(sha256('tist'::bytea), 'hex'), 2),
	(4, 95806698, 'Даниил', 'Олегович', 'Иванов', 'tast', 'ml_sotr1@internal.portal', encode(sha256('tast'::bytea), 'hex'), 3),
	(5, 58071201, 'Леонид', 'Нуборпшевич', 'Пахомов', 'tyst', 'guest@internal.portal', encode(sha256('tyst'::bytea), 'hex'), 7);


INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2c84c299-0dba-4f2a-9b3f-920803c17921', '5', '2', '4', 'in vero ullam', '2023-07-26T22:39:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('cf131632-a8fb-4221-a419-68cc169ea999', '5', '1', '5', 'nobis corporis quam', '2023-07-26T22:40:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('14976c6d-289f-4080-948e-12c979aa9a51', '3', '2', '2', 'commodi ab quibusdam', '2023-07-26T22:41:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('fa8006e1-77f9-4a42-8f65-08c0c726f94b', '3', '1', '4', 'nisi laboriosam deserunt', '2023-07-26T22:42:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7e5e8d1a-1f79-409f-8b84-d5383144a1ab', '3', '2', '5', 'excepturi est necessitatibus', '2023-07-26T22:43:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('20d2b2cb-e101-41d7-8bdc-daf9a05f803e', '3', '1', '6', 'maiores harum exercitationem', '2023-07-26T22:44:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('ef49f4e8-115b-4fe5-aaa2-620d0121377b', '5', '1', '4', 'dolores itaque modi', '2023-07-26T22:45:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e65441de-48ce-4630-88f9-4961949f9406', '2', '0', '3', 'provident pariatur voluptatibus', '2023-07-26T22:46:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('26a9e6a2-f309-4c4d-bb15-9c6a19d44f83', '3', '2', '1', 'expedita minima consequuntur', '2023-07-26T22:47:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('1b0f8fe8-559d-4127-9896-4e483759d951', '4', '2', '3', 'repellendus enim repudiandae', '2023-07-26T22:48:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('d0ebe5a3-cb68-4de4-b102-000f48cf5c49', '1', '1', '3', 'libero velit sint', '2023-07-26T22:49:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('d2195eff-b213-47c9-aa53-6262493ddf0b', '1', '1', '1', 'eum sunt beatae', '2023-07-26T22:50:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('8a8b35ba-8703-408e-9d41-269576bc4c13', '2', '1', '4', 'voluptas ex magni', '2023-07-26T22:51:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('eb1c9d0e-684b-4a3a-b169-7e7ed8949f3b', '5', '1', '5', 'aperiam nesciunt atque', '2023-07-26T22:52:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('8e0225c9-1d29-482f-9a12-f81e2005f2d8', '5', '0', '4', 'dolorum rerum corrupti', '2023-07-26T22:53:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('1bb53a86-7c3f-4864-b107-66a4feea15f2', '5', '2', '2', 'neque sequi quos', '2023-07-26T22:54:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c908805d-add2-4599-829e-8fe6af30121e', '1', '2', '6', 'sint error tenetur', '2023-07-26T22:55:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a6e71324-2c7f-46f2-a153-2e556616250a', '1', '2', '5', 'quam dolor quos', '2023-07-26T22:56:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('d6557316-e9ea-4d9a-8c8a-0526e536744a', '5', '0', '6', 'eveniet repellendus sapiente', '2023-07-26T22:57:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('db49cd2d-f0d9-458f-a36c-af07e1223dbd', '1', '1', '6', 'explicabo velit sapiente', '2023-07-26T22:58:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('afb92f9c-e904-4de2-b482-a48612b99bbe', '2', '2', '5', 'atque modi blanditiis', '2023-07-26T22:59:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('918a06ff-63a9-41ab-8603-4c268693bfdd', '3', '1', '2', 'necessitatibus dicta alias', '2023-07-26T23:00:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7eeb98b6-eab6-4649-b436-ea982d517b3e', '3', '0', '3', 'id mollitia hic', '2023-07-26T23:01:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c450da35-db56-47d8-8d43-ad692a7c62a0', '5', '0', '2', 'dolore itaque sit', '2023-07-26T23:02:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('477f2dbe-3f06-4193-b349-2c848335954f', '4', '0', '6', 'pariatur provident exercitationem', '2023-07-26T23:03:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('53221c30-8021-4e9d-bc3b-ae54821be895', '1', '2', '1', 'quos nam nobis', '2023-07-26T23:04:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('6124cf42-9379-4f3e-bb58-7d49633a802a', '1', '2', '6', 'velit repellat corporis', '2023-07-26T23:05:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('8d3f94be-1075-4d36-9cdc-c2412556ef5b', '4', '0', '5', 'magnam sequi officiis', '2023-07-26T23:06:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e654bb2c-22b9-4a44-806d-da5253d48419', '3', '2', '1', 'voluptate adipisci esse', '2023-07-26T23:07:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('629bd7f7-ae02-44e8-ae47-1df352f6dada', '5', '0', '3', 'voluptatibus voluptates reiciendis', '2023-07-26T23:08:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('6577ca63-18e6-4143-b637-d6d348837a6f', '3', '1', '6', 'delectus sed natus', '2023-07-26T23:09:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7c384f6d-fae7-46e2-a0e8-15e44c8ec08c', '5', '0', '4', 'adipisci similique consequatur', '2023-07-26T23:10:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('9493a3cf-4bb3-44b3-a6d3-f426dfdd398f', '4', '1', '5', 'nobis sed iusto', '2023-07-26T23:11:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a3981463-7139-45fa-9161-d6294416c0d8', '4', '2', '2', 'explicabo optio est', '2023-07-26T23:12:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7d648425-929c-4209-a6f3-4d76b9bbfd2f', '4', '1', '5', 'distinctio quam fuga', '2023-07-26T23:13:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2bc8dc33-4879-4798-8391-8b030824a66a', '2', '2', '5', 'delectus quis voluptatum', '2023-07-26T23:14:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e86e8002-322c-4cea-9897-2b8988aeb7fb', '4', '1', '3', 'soluta iusto repellat', '2023-07-26T23:15:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('32360d0f-23e0-475f-b489-90622ad02517', '5', '1', '5', 'rerum dicta aperiam', '2023-07-26T23:16:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c086039b-0429-4456-a1d3-05886c56b262', '3', '0', '6', 'culpa sed sed', '2023-07-26T23:17:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('f248de2d-9c79-4a88-8d57-e6c2662a89f9', '5', '1', '5', 'voluptatem recusandae optio', '2023-07-26T23:18:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e6839ab5-6c7d-4600-8fbc-e9c6f63fc287', '5', '2', '3', 'architecto assumenda in', '2023-07-26T23:19:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('693ab28a-cfdf-4a34-bb5f-15ccfeca10e2', '5', '1', '5', 'molestiae ipsam quidem', '2023-07-26T23:20:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('0350702d-79a2-4c15-85dc-4cb2f313aee0', '1', '2', '1', 'eveniet tempore optio', '2023-07-26T23:21:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('bc9f6797-a568-493e-b58f-dd1f683e2323', '4', '0', '2', 'qui vel hic', '2023-07-26T23:22:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('32a0d6c0-c6fa-42cf-9cca-725d85358013', '4', '0', '2', 'maxime ullam temporibus', '2023-07-26T23:23:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('5319f90a-f629-4ea8-ba00-f66cb8b6bf12', '5', '1', '1', 'maxime sint alias', '2023-07-26T23:24:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('397b0c1d-df54-4329-911f-81f4527feb45', '2', '0', '4', 'distinctio quae earum', '2023-07-26T23:25:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('55bfa3ca-2c11-4613-a6cf-2639015c5f7a', '4', '2', '3', 'quia vitae blanditiis', '2023-07-26T23:26:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('b7436986-fbe1-4f97-a183-a79614dc5ec4', '4', '2', '1', 'quo officia harum', '2023-07-26T23:27:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('342ef3e2-c5f4-4f06-a1ed-9ee666639ad5', '1', '0', '3', 'eum beatae beatae', '2023-07-26T23:28:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('6ef2e8f2-f7e5-4f44-8af7-5b891702e705', '1', '2', '3', 'eaque totam voluptate', '2023-07-26T23:29:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4364c94f-628f-437f-b88c-eea86d659e2c', '3', '2', '5', 'blanditiis ullam possimus', '2023-07-26T23:30:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('eb22a409-0552-42d0-8710-275443a5a3dd', '3', '2', '6', 'accusamus cumque veritatis', '2023-07-26T23:31:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('5aa4a9a8-af28-4dfb-a63a-d02b50c59037', '1', '0', '3', 'fuga autem nesciunt', '2023-07-26T23:32:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('80128bb4-a7c4-4803-bf1b-b02dc8dd253d', '5', '0', '1', 'doloremque quisquam officia', '2023-07-26T23:33:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('72b0ec69-0684-49c0-ade6-85012394d27b', '5', '0', '5', 'quos molestias illo', '2023-07-26T23:34:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('f286b2d5-5962-408c-ae5d-0405d326f927', '3', '2', '3', 'reiciendis pariatur harum', '2023-07-26T23:35:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('39c16b66-e016-4eec-8c36-82faa39f0b9e', '5', '0', '2', 'porro sint incidunt', '2023-07-26T23:36:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c3e5f9a6-517c-4349-a04d-b0b2ad1da635', '4', '2', '5', 'provident expedita eos', '2023-07-26T23:37:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c9029d6c-11b5-465c-8f8a-d26e7d10072b', '3', '2', '3', 'quae iste ipsa', '2023-07-26T23:38:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('0cb2dcb9-0b90-4ec5-9372-88fec605fdc5', '3', '1', '4', 'qui illo molestias', '2023-07-26T23:39:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('987501c3-d1a5-4d26-94f9-fe7ed99350c5', '2', '2', '1', 'cumque architecto delectus', '2023-07-26T23:40:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7805ea95-30ef-44c0-ad35-c125fb94cc5f', '2', '0', '1', 'corrupti ab dolores', '2023-07-26T23:41:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('009428b7-6dc0-4f3a-a7e8-4f462c4d016f', '1', '1', '4', 'adipisci a ad', '2023-07-26T23:42:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a98200e5-6e30-4042-b74c-7f9a3b4e6573', '2', '1', '3', 'asperiores adipisci rem', '2023-07-26T23:43:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('8fc4423e-9d47-4417-a0d8-91e74f0c9c91', '1', '0', '5', 'animi sapiente eos', '2023-07-26T23:44:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7bcbc0b3-9e5b-4ed2-a207-449c0691d3f3', '4', '0', '5', 'itaque quos laborum', '2023-07-26T23:45:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e4ea0cb4-1d75-4f6f-9ab1-4f63e093c040', '4', '2', '2', 'alias sapiente voluptatem', '2023-07-26T23:46:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('b21191fd-3c75-44eb-ad37-2a7d94d06365', '3', '2', '6', 'cum debitis nesciunt', '2023-07-26T23:47:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('983b2e43-ace9-464e-a7b0-03179bb965cd', '5', '2', '6', 'aliquid atque necessitatibus', '2023-07-26T23:48:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('b4d2b603-6610-4e06-87ea-e1d3b5ae103d', '5', '2', '2', 'quidem eveniet sunt', '2023-07-26T23:49:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('10cea895-cf13-4f47-8973-af1c11aba386', '5', '2', '1', 'inventore impedit eum', '2023-07-26T23:50:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('129dfa0c-41cb-40fc-832c-c7c17c38eef1', '5', '1', '1', 'nobis odio nesciunt', '2023-07-26T23:51:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('897cf258-54da-4b76-b889-9898d6b4d83c', '5', '1', '2', 'dolorem perspiciatis quia', '2023-07-26T23:52:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('42a089cd-5ba2-408b-9960-18f69e02060e', '5', '1', '1', 'odit est atque', '2023-07-26T23:53:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('5d7fdc33-de82-44b5-b118-fba411fedf42', '4', '1', '4', 'voluptatum voluptatum doloribus', '2023-07-26T23:54:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('6e01ac65-7232-4e30-91b1-43bc491cb474', '2', '1', '6', 'vitae necessitatibus maxime', '2023-07-26T23:55:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('6d955009-872f-4258-97ce-79ec7d3fbeb2', '2', '1', '4', 'eum in eum', '2023-07-26T23:56:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('615312b0-ab2b-43f3-874c-603e4803e04e', '5', '1', '5', 'ea provident libero', '2023-07-26T23:57:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('019c517b-76d1-4ff8-82d6-b0d15bca5649', '4', '1', '4', 'nam ex velit', '2023-07-26T23:58:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('74b2b3d7-b130-4706-a73b-a02933b42a84', '5', '1', '2', 'a enim dolorum', '2023-07-26T23:59:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('43500de6-b23d-4fbe-8a77-66cf04ccba06', '1', '1', '3', 'facere laboriosam rerum', '2023-07-27T00:00:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('f8825dc1-4a2d-4421-921f-9382c802c24d', '3', '2', '6', 'illo omnis voluptatibus', '2023-07-27T00:01:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2a91aa12-e57e-4505-a5b8-ccec9a6f79d3', '2', '1', '4', 'dicta tempore alias', '2023-07-27T00:02:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('8bc4dde5-7619-4876-a8e6-e2aa647efeb2', '5', '0', '6', 'enim sint quaerat', '2023-07-27T00:03:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('490f443b-6089-4a38-937a-d1e61d433ee6', '5', '0', '1', 'dolorem corrupti aut', '2023-07-27T00:04:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('ab156870-707a-4815-90a7-e75e58eb187a', '1', '1', '5', 'occaecati cumque modi', '2023-07-27T00:05:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4da09061-db72-4d29-9870-921778a6d276', '5', '1', '4', 'placeat modi dolores', '2023-07-27T00:06:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('56f6ddd0-8c45-4ee6-a9ff-a9936911a7e8', '2', '1', '4', 'reprehenderit soluta earum', '2023-07-27T00:07:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7f8b072a-50bb-4d08-9e85-b710b48d1132', '3', '1', '6', 'voluptates dolor libero', '2023-07-27T00:08:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('bb021210-9849-4af4-9a63-026a41a01385', '2', '2', '1', 'dolor impedit a', '2023-07-27T00:09:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('863f16a1-9efd-47ea-aad8-855e5645dcf4', '2', '2', '3', 'aliquam totam distinctio', '2023-07-27T00:10:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('b06cabbc-e84c-42f9-85d5-4cbbcdb2eb37', '3', '1', '2', 'eligendi cumque nulla', '2023-07-27T00:11:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('f6eb4f40-aaca-4583-b9e7-df7440accae0', '2', '1', '5', 'nisi officia natus', '2023-07-27T00:12:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c7067677-d5f4-4755-acaf-ba9bc4cd2bab', '4', '1', '6', 'eum facere ullam', '2023-07-27T00:13:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('aec0e535-783b-41d9-a883-b112a7f32904', '3', '1', '3', 'reiciendis officia doloremque', '2023-07-27T00:14:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4d255bb5-5a31-472d-8cd2-c28e32177c25', '3', '2', '3', 'aliquid ad dignissimos', '2023-07-27T00:15:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('589617b6-a618-4802-bddf-7a1659c036bf', '5', '1', '6', 'aperiam corrupti eveniet', '2023-07-27T00:16:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('20f26a45-7175-450a-85ed-c84d78cf763f', '1', '2', '1', 'aperiam aut excepturi', '2023-07-27T00:17:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('87fce564-7144-4f83-a6e8-e4c4d3b941e8', '2', '2', '6', 'molestiae enim fuga', '2023-07-27T00:18:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('8c8ed7bc-6858-4f0b-9da9-1ec31629331d', '4', '1', '4', 'earum sunt provident', '2023-07-27T00:19:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('cdb5effa-0da1-4af8-a08b-4ad4e67ceada', '4', '2', '3', 'veritatis adipisci alias', '2023-07-27T00:20:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('3b3f0ed5-47e0-4c6d-9934-ae13856d19b2', '4', '1', '3', 'libero sed adipisci', '2023-07-27T00:21:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7b4e87d4-f740-4f52-9844-097dccec37f9', '3', '0', '6', 'laboriosam nam expedita', '2023-07-27T00:22:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4b0a18fe-5450-45a3-bb17-43be064c897f', '1', '2', '3', 'veniam dignissimos maxime', '2023-07-27T00:23:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a265c617-4195-4c0a-9a0b-205d92f30fc2', '3', '0', '6', 'iusto eveniet incidunt', '2023-07-27T00:24:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('b58841d8-81b6-471c-a48a-5a4bbb4602fd', '1', '1', '3', 'odio recusandae quos', '2023-07-27T00:25:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('b13fe603-33d9-4877-901e-1f757abfbab0', '1', '2', '1', 'aut voluptas molestias', '2023-07-27T00:26:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('94e55386-9d07-4828-80c7-f66b0e24fc57', '3', '0', '6', 'mollitia odit cumque', '2023-07-27T00:27:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a0bacdb2-0807-4bb3-9b9a-90a6e42a95a8', '3', '0', '2', 'ullam ullam dolor', '2023-07-27T00:28:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('19622db8-514f-48b7-a656-fcb15812694d', '1', '2', '3', 'aliquid vero dolor', '2023-07-27T00:29:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('1a3230d1-7ca2-44b9-a0ab-2e8f5b4724e0', '4', '1', '1', 'veritatis provident esse', '2023-07-27T00:30:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('6b18c833-15ff-402a-a5bf-f56a83520e2b', '2', '2', '2', 'eligendi at accusantium', '2023-07-27T00:31:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('56fa5f53-f7e2-4ab2-942b-78335350ff65', '5', '2', '6', 'ducimus natus porro', '2023-07-27T00:32:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a08ea2b8-ce25-4fdd-bb00-5ae3305d1e58', '3', '0', '5', 'repudiandae distinctio repellendus', '2023-07-27T00:33:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2f7ee1d7-c63e-4f3e-b7f9-ecd274ad8102', '4', '2', '5', 'corporis saepe aperiam', '2023-07-27T00:34:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('aa6cdeb9-01af-4fc5-8d3a-12b0f6678637', '1', '0', '3', 'autem deserunt natus', '2023-07-27T00:35:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('9acccecb-d631-40dc-94b6-050c8127772b', '5', '1', '3', 'repellat quibusdam facilis', '2023-07-27T00:36:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e265323e-3a8b-44f6-8f54-80d7dd1cf648', '2', '0', '4', 'saepe corrupti eaque', '2023-07-27T00:37:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('fc13d94b-f9db-485f-ae9d-be88cb06dd0d', '4', '0', '2', 'officia veniam nam', '2023-07-27T00:38:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4c27eaae-3192-4583-b485-d8da3fb78751', '5', '1', '2', 'sunt atque beatae', '2023-07-27T00:39:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('215e04dc-4710-4805-b835-b901816d6f46', '2', '0', '2', 'at nemo accusamus', '2023-07-27T00:40:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('1086d6a1-ed5f-47cf-8bf1-df8122f958d9', '3', '0', '3', 'inventore facere recusandae', '2023-07-27T00:41:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('52c8efc3-797a-4f78-bcc0-bb1c62d81e5a', '5', '0', '1', 'porro ipsum vero', '2023-07-27T00:42:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a5207fd1-b755-4f4b-b4e9-875845bbc8cd', '1', '1', '6', 'ratione laboriosam exercitationem', '2023-07-27T00:43:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c220fc9c-8dc1-4d24-965b-043f93ae965c', '1', '1', '2', 'mollitia eius tenetur', '2023-07-27T00:44:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('3127f83d-d721-4838-b74d-a55b9a5b1749', '3', '1', '1', 'aspernatur adipisci dolores', '2023-07-27T00:45:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a762868e-0b54-46e6-825d-cf57510ab5a0', '3', '1', '2', 'iure aliquid cupiditate', '2023-07-27T00:46:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('ff30eacc-1518-4c20-a8c3-5e3c6a2d7495', '5', '1', '5', 'harum expedita quidem', '2023-07-27T00:47:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a0b88b90-cc07-4d5b-9795-20d2df80668d', '2', '1', '3', 'excepturi sapiente suscipit', '2023-07-27T00:48:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('57b558e5-5ce0-42d9-8297-f48a1e731e0c', '3', '2', '3', 'est aut omnis', '2023-07-27T00:49:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('fdd9c927-586c-4422-b923-6ce44661f501', '2', '1', '6', 'repudiandae facilis blanditiis', '2023-07-27T00:50:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('dd044011-668a-4943-b5a3-2f427fdfb48a', '2', '1', '5', 'maxime cupiditate officia', '2023-07-27T00:51:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('96a1b44b-9a74-4eee-8d78-2d00a256b04f', '4', '0', '2', 'voluptas assumenda natus', '2023-07-27T00:52:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('b59b4a39-473a-4a4c-b3db-ea26f35c9aa4', '4', '2', '1', 'maiores eum nihil', '2023-07-27T00:53:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c7730313-dd01-4376-88c2-ba232739c501', '2', '1', '2', 'nobis magni repellendus', '2023-07-27T00:54:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('0ba66116-5e17-4f98-b68b-fa7cbcc3d3ae', '3', '0', '3', 'corporis nostrum laudantium', '2023-07-27T00:55:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c3366b91-0440-4a8d-87ad-46570fce85c4', '4', '1', '5', 'nostrum quisquam cupiditate', '2023-07-27T00:56:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('bc7ad4b2-2c7f-4b89-a636-0234cec65985', '1', '1', '3', 'nesciunt repudiandae rerum', '2023-07-27T00:57:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('89f768e0-2e81-4d8a-a162-c5144d954edb', '2', '0', '6', 'tempora cumque dignissimos', '2023-07-27T00:58:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('369a15cd-d522-4e5e-b6e1-c10e60f1e172', '3', '1', '5', 'quisquam eligendi voluptatum', '2023-07-27T00:59:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2bfd4222-354c-4c5f-973a-e28ae09721e3', '3', '2', '1', 'exercitationem nihil minus', '2023-07-27T01:00:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('9a0eade1-8060-4dc4-b91f-c1c65d4a0f85', '5', '1', '3', 'sunt ut explicabo', '2023-07-27T01:01:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('810e67af-f11e-4d77-b02a-95e80556705c', '5', '1', '6', 'ullam praesentium magnam', '2023-07-27T01:02:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('3bb1ea41-4e61-4f24-92f1-066aa2ddfc66', '4', '1', '5', 'expedita velit veniam', '2023-07-27T01:03:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4d6990cd-335d-4c61-ab8f-38e0f1588c64', '1', '0', '2', 'veritatis sint magnam', '2023-07-27T01:04:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('3d4c097c-1a8d-4e22-b82a-96df40338eec', '1', '1', '1', 'eos occaecati nisi', '2023-07-27T01:05:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('558c131a-261f-4f51-925c-bd906d06f299', '3', '1', '4', 'fugiat et harum', '2023-07-27T01:06:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('97598ba4-e098-4176-9c93-28dd53022b09', '5', '2', '5', 'consectetur sed maiores', '2023-07-27T01:07:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('8b655816-349d-49f6-9942-aa27ba035081', '2', '1', '4', 'animi quae ratione', '2023-07-27T01:08:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('fde23590-d204-4418-a7ef-1cf80803b00c', '3', '0', '1', 'velit tempore libero', '2023-07-27T01:09:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('26aa9a45-883b-4a2a-95cf-e4fd78836c5a', '2', '2', '6', 'nemo aperiam eveniet', '2023-07-27T01:10:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2211c542-3a07-47f2-bb92-65a4e313fbc1', '1', '2', '2', 'occaecati nisi in', '2023-07-27T01:11:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e724281c-999b-4eee-852f-1ac4dc2a1800', '2', '0', '2', 'quae suscipit quasi', '2023-07-27T01:12:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('1fad0db4-e0d3-4362-91f2-c5d1da5cb7bf', '3', '0', '5', 'illum cupiditate quidem', '2023-07-27T01:13:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('6be48d93-f7b9-43e0-82ba-04be4c853e59', '3', '0', '5', 'illum magni vitae', '2023-07-27T01:14:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('d9180380-3b19-4818-9d2b-97dcb6fb0230', '3', '1', '5', 'nisi natus inventore', '2023-07-27T01:15:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c8a49cfc-04e0-4513-b280-88a43842af46', '3', '2', '4', 'illo minus fugit', '2023-07-27T01:16:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4da69605-178e-4041-8309-da10fb11f9b2', '3', '2', '3', 'libero veritatis doloribus', '2023-07-27T01:17:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('f8f54775-f4d6-4114-ac2e-aeff82d4451e', '5', '1', '1', 'ex quidem dolores', '2023-07-27T01:18:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2fbde5d8-1e3e-4d91-9312-642838236637', '4', '2', '3', 'iste suscipit minus', '2023-07-27T01:19:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('3690e402-636d-4fc3-bd9c-f95aff00914f', '1', '1', '1', 'sed ducimus at', '2023-07-27T01:20:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c5892101-9a89-4016-80da-e73ed9760484', '4', '1', '6', 'blanditiis ullam at', '2023-07-27T01:21:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('ebccdf0c-d95e-4fff-b039-fd61ec0f0283', '2', '0', '1', 'tenetur eveniet at', '2023-07-27T01:22:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a523c2f0-859e-4568-af69-5b1571bc371e', '5', '2', '2', 'atque sequi doloribus', '2023-07-27T01:23:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4e526c0e-5552-43b0-9768-b3bb07505812', '1', '0', '4', 'quis modi commodi', '2023-07-27T01:24:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('140ec622-ebd1-478f-ba5f-6820d999efca', '4', '1', '2', 'commodi architecto numquam', '2023-07-27T01:25:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2ff1f6cb-fc01-47a3-8196-ff1f068a0c28', '2', '1', '6', 'aliquid molestias fuga', '2023-07-27T01:26:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('c6bcced3-e67c-4753-9dbe-215ac9c5c974', '2', '0', '1', 'magni officiis praesentium', '2023-07-27T01:27:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('d2d8df50-8845-48a3-a7c5-910d7570a4b4', '4', '1', '3', 'officiis voluptate tempore', '2023-07-27T01:28:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('bc8515c6-2ad4-4509-967d-0af69f351289', '4', '0', '5', 'earum in culpa', '2023-07-27T01:29:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7c8f210e-ef1a-4c1a-b8ad-f1579917e878', '3', '2', '5', 'culpa fugit incidunt', '2023-07-27T01:30:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('d715dce1-cedc-4d75-ae9a-41ce3aa5dd3e', '2', '2', '3', 'animi magnam eaque', '2023-07-27T01:31:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('0c7ef4f9-5e58-4c8c-b80b-9263c18f30a7', '3', '2', '5', 'facilis vel excepturi', '2023-07-27T01:32:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('176c4c37-6186-4efa-848a-c2ae02d2f719', '4', '1', '1', 'esse harum doloribus', '2023-07-27T01:33:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('437cc4be-d22f-491e-9222-ac68b0f8e494', '1', '2', '5', 'dolorum cum fugit', '2023-07-27T01:34:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('741a53d0-a529-471a-aac9-fce3dce94e0d', '4', '0', '4', 'illo inventore sequi', '2023-07-27T01:35:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('7362053d-5ddc-40ed-9241-dbd1ae4db022', '4', '2', '1', 'laboriosam voluptates minima', '2023-07-27T01:36:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('1a3846c3-072d-4bae-873f-26aab60b0ea4', '5', '0', '1', 'autem facilis dolores', '2023-07-27T01:37:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2ec4685d-8eb4-44a6-b674-03ef2c5f0ad0', '4', '2', '1', 'esse odit distinctio', '2023-07-27T01:38:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('910659c2-4754-4243-bb1b-e2295930b423', '5', '0', '1', 'doloremque consequuntur deserunt', '2023-07-27T01:39:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('d3d2bcb1-8f98-45a8-9a19-e24dc548960c', '3', '2', '2', 'quod esse numquam', '2023-07-27T01:40:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('49a0a3f1-6ca3-4667-b96c-ddbf0e944d45', '5', '2', '6', 'natus maiores omnis', '2023-07-27T01:41:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('2ad7c3e1-c466-4665-a44c-efc1826e1851', '1', '2', '5', 'tenetur explicabo dolor', '2023-07-27T01:42:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('5f40b8a8-4d3b-42d5-910a-9bfdfaaf47be', '4', '1', '6', 'quos esse debitis', '2023-07-27T01:43:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e2faf447-841a-4c0e-bb6b-76138e4cf220', '4', '0', '5', 'eum dolore quis', '2023-07-27T01:44:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('419b6330-526c-4d3f-a7e8-3d974ce1ea27', '5', '1', '1', 'reiciendis placeat corrupti', '2023-07-27T01:45:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('ea1a90e1-6e28-402d-8b1e-5497775bc085', '1', '0', '2', 'placeat necessitatibus assumenda', '2023-07-27T01:46:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4331c03c-a5ed-4160-8f18-9482975d3f2e', '1', '1', '2', 'dolore deleniti amet', '2023-07-27T01:47:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('326f39d2-23d4-41ba-a3f1-37652ac2d6dc', '2', '1', '3', 'corrupti perferendis nisi', '2023-07-27T01:48:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('5ba4c9e4-61f7-4303-accb-06c90b9afa4f', '5', '0', '6', 'quam nisi sit', '2023-07-27T01:49:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('455a1495-3fb4-48ea-97b2-6a6c6b42dfac', '1', '1', '1', 'ipsa sed minima', '2023-07-27T01:50:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('dbc0733d-f1f3-48b2-975f-b9e95838d179', '3', '0', '1', 'accusamus labore magni', '2023-07-27T01:51:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('98ef2cc3-48f2-408e-aee8-e5bd65c39fae', '2', '0', '2', 'adipisci veniam itaque', '2023-07-27T01:52:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('d950c602-e6f7-4113-9fa1-01e8f62bdd5d', '5', '1', '4', 'voluptatum facilis eum', '2023-07-27T01:53:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a5029d64-a88c-49d8-8a8b-835806002914', '4', '1', '3', 'laboriosam corrupti architecto', '2023-07-27T01:54:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('4f39d7d1-5578-45b6-a192-9b03228f0c00', '1', '1', '5', 'voluptatem saepe nesciunt', '2023-07-27T01:55:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('a6f14a5e-3bf2-4066-a94e-760fb69cfd39', '1', '1', '4', 'molestias ad ea', '2023-07-27T01:56:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e696b29e-b833-4571-83d8-3f5f56c736e6', '2', '0', '6', 'soluta saepe inventore', '2023-07-27T01:57:53.257');
INSERT INTO tickets (uuid, reporter_id, priority_id, problem_id, text, created_at) VALUES ('e853e6b2-65c6-413b-861e-b2f8dad337cb', '2', '0', '3', 'minima quos dolor', '2023-07-27T01:58:53.257');