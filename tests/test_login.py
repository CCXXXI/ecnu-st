def test_login(driver):
    """Redirected to /home after login"""
    assert driver.current_url.endswith("/home")
