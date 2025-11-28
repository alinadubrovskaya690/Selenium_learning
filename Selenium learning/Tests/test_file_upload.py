from Pages.file_upload_page import FileUploadPage

def test_file_upload(browser):
    file_upload_pg = FileUploadPage(browser)
    file_upload_pg.file_upload_open()
    file_upload_pg.choose_file_button("C:/Documents/Info/Gemia/Palette.png")
    file_upload_pg.submit_button()
    assert file_upload_pg.submit_alert_is_displayed() == True