from unfold.sites import UnfoldAdminSite


class EditorAdminSite(UnfoldAdminSite):
    site_header = "Редактор статей"
    site_title = "Редактор"
    index_title = "Панель редактора"
    site_url = None  # Убираем ссылку "View site"

class PublisherAdminSite(UnfoldAdminSite):
    site_header = "Издатель статей"
    site_title = "Издатель"
    index_title = "Панель издателя"
    site_url = None

class ArchiveAdminSite(UnfoldAdminSite):
    site_header = "Архив статей"
    site_title = "Архив"
    index_title = "Панель архивариуса"
    site_url = None

# Создаем экземпляры админ-сайтов
editor_admin = EditorAdminSite(name='editor_admin')
publisher_admin = PublisherAdminSite(name='publisher_admin')
archive_admin = ArchiveAdminSite(name='archive_admin')
