Курсовая работа № 6 "Основы веб-разработки на Django"

Разработан сервис управления рассылками на основе сайта знакомств.
Сервис включает в себя: создание рассылки, управление, администрирования и сбора статистики.

Интерфейс содержит:
1) главная страница, на ней отображаются: 3 блоговых записи, реклама приложения для знакомств 
и статистическую информацию о рассылках;
2) приложение для знакомств: на странице отображаются пользователи, которым можно ставить лайки.
В базу данных заносится информация о пользователе кто поставил лайк и о пользователе кому поставили лайк, если 
их лайки взаимны, происходит мэтч и отправка уведомления(на стадии разработки);
статистическая информация о рассылках: здесь выводится вся статистическая информация о рассылках - количество рассылок на данный момент,
наших уникальных клиентов для рассылки, количество активных рассылок;
3) блог содержит блоговые записи, которые ведет контент-менеджер. Обычным пользователям доступен только просмотр;
4) профиль пользователя, который можно редактировать;
5) реализован функционал рассылок: создание группы пользователей для отправки, создания рассылки по периодичности, редактирование совей рассылки
6) реализован функционал управления: контент и рассылки. Менеджер по рассылкам может добавлять в черный список 
компанию или рассылку - в таком случае она не будет отправлена пользователю