GO
INSERT INTO users (name, email, password, pay_info, balance) VALUES
('John Doe', 'john.doe@example.com', 'password123', 'Visa ****1234', 1000.00),
('Jane Smith', 'jane.smith@example.com', 'qwerty2023', 'Mastercard ****5678', 500.25),
('Alice Brown', 'alice.brown@example.com', 'alicePass1', 'PayPal alice_brown', 300.75),
('Bob White', 'bob.white@example.com', 'bobSecure99', 'Amex ****4321', 1200.50),
('Charlie Black', 'charlie.black@example.com', 'charlie123!', 'Discover ****9876', 150.00),
('Emily Green', 'emily.green@example.com', 'emilyStrong22', 'Stripe emily_green', 750.00),
('Frank Blue', 'frank.blue@example.com', 'frankPass55', 'Visa ****6543', 0.00),
('Grace Yellow', 'grace.yellow@example.com', 'yellowGrace88', 'Cash', 450.00);

GO
INSERT INTO transactions (user_id, creation_date, done) VALUES
(1, '2024-12-01', 1),  -- Done set to 1 (true) explicitly
(2, '2024-12-02', 0),  -- Done set to 0 (false) explicitly
(3, '2024-12-03', 1),  -- Done set to 1 (true) explicitly
(4, '2024-12-04', 0),  -- Done uses default (0)
(5, '2024-12-05', 0),  -- Done uses default (0)
(6, '2024-12-06', 1),  -- Done set to 1 (true) explicitly
(7, '2024-12-07', 0),  -- Done uses default (0)
(8, '2024-12-08', 0);  -- Done set to 0 (false) explicitly

GO
INSERT INTO developers (email, password, name, contact_info, website) VALUES
('dev.john@example.com', 'johnDev123', 'John Dev', 'Phone: 123-456-7890', 'www.johndev.com'),
('dev.jane@example.com', 'janeSecure!', 'Jane Dev', 'Email: contact@janedev.com', 'www.janedev.com'),
('dev.alice@example.com', 'aliceCode42', 'Alice Dev', 'Phone: 987-654-3210', 'www.alicedev.com'),
('dev.bob@example.com', 'bobTheDev77', 'Bob Dev', 'Email: bob@devmail.com', 'www.bobdev.com'),
('dev.charlie@example.com', 'charliePass09', 'Charlie Dev', 'Phone: 111-222-3333', 'www.charliedev.com'),
('dev.emily@example.com', 'emilyWork88', 'Emily Dev', 'Email: emily@devmail.com', 'www.emilydev.com'),
('dev.frank@example.com', 'frankStrong55', 'Frank Dev', 'Phone: 444-555-6666', 'www.frankdev.com'),
('dev.grace@example.com', 'graceBuild11', 'Grace Dev', 'Email: grace@devworld.com', 'www.gracedev.com');


GO
INSERT INTO categories (cat_name, cat_description) VALUES
('Productivity', 'Tools to boost efficiency'),
('Entertainment', 'Games and media apps'),
('Health & Fitness', 'Apps for health tracking'),
('Education', 'Learning and study tools'),
('Travel', 'Travel planning and guides'),
('Finance', 'Expense tracking and budgeting'),
('Weather', 'Apps for weather updates'),
('Photography', 'Photo editing and camera tools');


GO
INSERT INTO apps (name, cat_name, app_version, release_date, downloads, price, app_description, dev_id, app_path, icon_path) VALUES
('TaskManager', 'Productivity', 1.001, '2024-01-15', 1000, 0.00, 'Task management app', 1, '/apps/taskmanager.exe', '/icons/taskmanager.png'),
('WeatherPro', 'Weather', 2.015, '2023-11-10', 5000, 1.99, 'Advanced weather app', 2, '/apps/weatherpro.exe', '/icons/weatherpro.png'),
('PhotoEditor', 'Photography', 3.500, '2024-02-20', 750, 9.99, 'Photo editing tool', 3, '/apps/photoeditor.exe', '/icons/photoeditor.png'),
('BudgetTracker', 'Finance', 4.002, '2023-09-05', 2000, 0.00, 'Expense tracking app', 4, '/apps/budgettracker.exe', '/icons/budgettracker.png'),
('GameMaster', 'Entertainment', 1.123, '2023-12-01', 15000, 4.99, 'Gaming assistant app', 5, '/apps/gamemaster.exe', '/icons/gamemaster.png'),
('HealthPlus', 'Health & Fitness', 1.010, '2024-03-11', 850, 2.49, 'Health and fitness app', 6, '/apps/healthplus.exe', '/icons/healthplus.png'),
('StudyBuddy', 'Education', 2.050, '2024-04-01', 1200, 0.00, 'Study aid for students', 7, '/apps/studybuddy.exe', '/icons/studybuddy.png'),
('TravelGuide', 'Travel', 3.001, '2023-08-15', 3000, 5.99, 'Travel planning app', 8, '/apps/travelguide.exe', '/icons/travelguide.png');

GO
INSERT INTO reviews (user_id, app_id, rating, review_text, review_date) VALUES
(1, 1, 5, 'Great task management app!', '2024-12-01'),
(2, 2, 4, 'Useful weather updates, but could be better.', '2024-12-02'),
(3, 3, 5, 'Love the photo editing features!', '2024-12-03'),
(4, 4, 3, 'Decent app, but lacks some features.', '2024-12-04'),
(5, 5, 4, 'Good game assistant, fun to use.', '2024-12-05'),
(6, 6, 5, 'Perfect for tracking my workouts!', '2024-12-06'),
(7, 7, 2, 'Doesn’t have enough study materials.', '2024-12-07'),
(8, 8, 5, 'Fantastic travel guide with great tips!', '2024-12-08');

GO
INSERT INTO apps_trans (trans_id, app_id) VALUES
(1, 1),  -- Transaction 1, App 1
(1, 3),  -- Transaction 1, App 3
(2, 2),  -- Transaction 2, App 2
(2, 4),  -- Transaction 2, App 4
(3, 5),  -- Transaction 3, App 5
(4, 6),  -- Transaction 4, App 6
(5, 7),  -- Transaction 5, App 7
(6, 8);  -- Transaction 6, App 8


/*=============================or you can use the procedures========================================*/
GO
DECLARE @UserSignUpResult INT;

EXEC @UserSignUpResult = UserSignUp 'JohnDoe', 'johndoe@example.com', 'password123', 'VISA-1234', 100.00;
EXEC @UserSignUpResult = UserSignUp 'JaneSmith', 'janesmith@example.com', 'password456', 'MASTERCARD-5678', 200.50;
EXEC @UserSignUpResult = UserSignUp 'AliceBrown', 'alicebrown@example.com', 'password789', NULL, 50.00;
EXEC @UserSignUpResult = UserSignUp 'BobWhite', 'bobwhite@example.com', 'securepass1', 'AMEX-9012', 75.75;
EXEC @UserSignUpResult = UserSignUp 'CarolKing', 'carolking@example.com', 'strongpass2', NULL, 150.25;
EXEC @UserSignUpResult = UserSignUp 'DavidClark', 'davidclark@example.com', 'password234', 'VISA-5678', 300.00;
EXEC @UserSignUpResult = UserSignUp 'EveAdams', 'eveadams@example.com', 'securepass3', NULL, 400.00;
EXEC @UserSignUpResult = UserSignUp 'FrankHill', 'frankhill@example.com', 'password678', 'PAYPAL-3456', 50.00;
EXEC @UserSignUpResult = UserSignUp 'GraceKelly', 'gracekelly@example.com', 'mypassword', NULL, 600.00;
EXEC @UserSignUpResult = UserSignUp 'HannahLee', 'hannahlee@example.com', 'strongpassword', 'BITCOIN-7890', 100.00;


GO
DECLARE @DevSignUpResult INT;

EXEC @DevSignUpResult = DevSignUp 'DevOne', 'dev1@example.com', 'devpass1', '123-456-7890', 'http://devone.com';
EXEC @DevSignUpResult = DevSignUp 'DevTwo', 'dev2@example.com', 'devpass2', '234-567-8901', 'http://devtwo.com';
EXEC @DevSignUpResult = DevSignUp 'DevThree', 'dev3@example.com', 'devpass3', '345-678-9012', 'http://devthree.com';
EXEC @DevSignUpResult = DevSignUp 'DevFour', 'dev4@example.com', 'devpass4', NULL, 'http://devfour.com';
EXEC @DevSignUpResult = DevSignUp 'DevFive', 'dev5@example.com', 'devpass5', '456-789-0123', NULL;
EXEC @DevSignUpResult = DevSignUp 'DevSix', 'dev6@example.com', 'devpass6', '567-890-1234', 'http://devsix.com';
EXEC @DevSignUpResult = DevSignUp 'DevSeven', 'dev7@example.com', 'devpass7', NULL, 'http://devseven.com';
EXEC @DevSignUpResult = DevSignUp 'DevEight', 'dev8@example.com', 'devpass8', '678-901-2345', NULL;
EXEC @DevSignUpResult = DevSignUp 'DevNine', 'dev9@example.com', 'devpass9', NULL, 'http://devnine.com';
EXEC @DevSignUpResult = DevSignUp 'DevTen', 'dev10@example.com', 'devpass10', '789-012-3456', 'http://devten.com';



GO
INSERT INTO categories (cat_name, cat_description) VALUES 
('Games', 'Fun and interactive games'),
('Education', 'Apps for learning and education'),
('Productivity', 'Tools to improve productivity'),
('Entertainment', 'Movies, music, and more'),
('Health', 'Health and fitness apps'),
('Finance', 'Manage your money better'),
('Photography', 'Edit and manage photos'),
('Social', 'Stay connected with friends'),
('News', 'Get the latest updates'),
('Utilities', 'Useful everyday tools');


GO
DECLARE @DevAddAppResult INT;

EXEC @DevAddAppResult = DevAddApp 'GameOne', 'Games', 1.0, 15.00, 'Exciting action game', 1, 'path/to/gameone', 'path/to/icongameone';
EXEC @DevAddAppResult = DevAddApp 'GameTwo', 'Games', 1.1, 20.00, 'Adventure game', 2, 'path/to/gametwo', 'path/to/icongametwo';
EXEC @DevAddAppResult = DevAddApp 'PhotoEditor', 'Photography', 2.0, 25.00, 'Advanced photo editing tool', 3, 'path/to/photoeditor', 'path/to/iconphotoeditor';
EXEC @DevAddAppResult = DevAddApp 'NewsToday', 'News', 1.0, 0.00, 'Get daily news updates', 4, 'path/to/newstoday', 'path/to/iconnewstoday';
EXEC @DevAddAppResult = DevAddApp 'HealthTracker', 'Health', 3.0, 10.00, 'Track your health goals', 5, 'path/to/healthtracker', 'path/to/iconhealthtracker';
EXEC @DevAddAppResult = DevAddApp 'FinancePro', 'Finance', 2.5, 30.00, 'Manage your finances', 6, 'path/to/financepro', 'path/to/iconfinancepro';
EXEC @DevAddAppResult = DevAddApp 'SocialHub', 'Social', 4.0, 0.00, 'Connect with friends', 7, 'path/to/socialhub', 'path/to/iconsocialhub';
EXEC @DevAddAppResult = DevAddApp 'MusicPlayer', 'Entertainment', 1.2, 5.00, 'Stream your favorite music', 8, 'path/to/musicplayer', 'path/to/iconmusicplayer';
EXEC @DevAddAppResult = DevAddApp 'CodeEditorX', 'Productivity', 3.2, 0.00, 'Code editor with syntax highlighting', 9, 'path/to/codeeditorx', 'path/to/iconcodeeditorx';
EXEC @DevAddAppResult = DevAddApp 'UtilityTool', 'Utilities', 1.5, 7.50, 'Useful everyday tool', 10, 'path/to/utilitytool', 'path/to/iconutilitytool';



GO
EXEC AddToCart 1,1
EXEC AddToCart 1,2

EXEC AddToCart 2,3
EXEC AddToCart 2,4

/**/

GO
EXEC addReview 1, 1, 5, 'Amazing game!';
EXEC addReview 2, 3, 4, 'Great photo editor';
EXEC addReview 3, 5, 5, 'Very useful app';
EXEC addReview 4, 7, 3, 'Good app but can improve';
EXEC addReview 5, 9, 4, 'Helpful for coding tasks';
EXEC addReview 1, 2, 5, 'Loved the adventure!';
EXEC addReview 2, 4, 4, 'Informative news';
EXEC addReview 3, 6, 4, 'Easy to track finances';
EXEC addReview 4, 8, 3, 'Decent music player';
EXEC addReview 5, 10, 5, 'Very useful tool!';


