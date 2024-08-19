import time
import base64
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class gameflow():
    middle_screen_x = 800
    middle_screen_y = 1300
    
    #Announcements
    announcements_board_close_btn = (middle_screen_x, 2400)
    announcement_close_btn = (1200, 2030)
    login_bonus_confirm_btn = (middle_screen_x, 2400)
    login_bonus_close_btn = (middle_screen_x, 1800)
    
    #Main
    main_btn = (190,2460)
    main_portal = (400,1230)
    main_arena = (400, 1700)
    main_invasion = (1000, 1050)
    main_secondary_screen_btn = (1450, 2090)
    main_primary_screen_btn = (1450, 2090)

    #Portal
    portal_swipe_down = (middle_screen_x, 2100, middle_screen_x, 60, 200)
    portal_swipe_up = (middle_screen_x, 1000, middle_screen_x, 1800, 2000)
    portal_energy_mission = (middle_screen_x, 1350)
    portal_coins_mission = (middle_screen_x, 1900)
    portal_choose_mision = (middle_screen_x, 1070)
    portal_mision_option_sweep = (middle_screen_x, 2000)
    portal_mission_max_btn = (1400, 1200)
    portal_mission_sweep_btn = (middle_screen_x, 1750)
    portal_mission_close_btn = (middle_screen_x, 1930)
    portal_mission_goback = (200, 2230)

    #Invasion
    invasion_challenge_btn = (middle_screen_x, 2100)
    invasion_battle_btn = (middle_screen_x, 2200)
    invasion_battle_ends_confirm = (middle_screen_x, 2400)
    invasion_goback_btn = (200, 2500)

    #Arena
    arena_mode_arena = (500, middle_screen_y)
    arena_choose_opponent = (1200, 1400)
    
    #Grand Arena 
    arena_mode_g_arena = (1100, middle_screen_y)
    g_arena_reward = (1400, 600)
    g_arena_reward_claim = (middle_screen_x, 1600)
    g_arena_reward_close = (middle_screen_x, 1800)
    g_arena_choose_opponent = (1200, 1550)
    g_arena_opponent_free = (1100, 2300)
    g_arena_next_team = (middle_screen_x, 2400)
    g_arena_battle_finish_confirm = (middle_screen_x, 2400)
    g_arena_go_back_btn = (200, 2500)

    def __init__(self, driver, wait, repo_path) -> None:
        self.driver = driver
        self.wait = wait
        self.repo_path = repo_path

    def load_image(self, image_name):
        with open(rf"{self.repo_path}/appium/images/{image_name}", "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
        return image_base64

    def open_app(self, package_name):
        self.driver.terminate_app(package_name)
        self.driver.activate_app(package_name)
        # Waiting app to be opened and ready to use
        print("Esperando por la applicacion para abrir")
        self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=self.load_image("enter_btn.jpg")))
        time.sleep(3)
        TouchAction(self.driver).tap(None, 809, 2329,1).perform()
        print("Esperando por pantalla inicial")

    def close_initial_game_announcements(self):
        #Esperando a que entremos a la pantalla principal

        announcement_close_btn_img = self.load_image("close_announcement_btn.jpg")
        announcements_board_img = self.load_image("announcements_board.jpg")
        login_bonus_img = self.load_image("login_bonus.jpg")
        main_screen_img = self.load_image("main_screen_1.jpg")
        short_wait = WebDriverWait(self.driver,5)
        
        try:
            print("Esperando página de login bonus")
            self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=login_bonus_img))
            print("Página de Login bonus encontrada...")
            while True:
                try:
                    print("Confirmando premio de login bonus")
                    TouchAction(self.driver).tap(None,*self.login_bonus_confirm_btn,1).perform()
                    time.sleep(2)
                    TouchAction(self.driver).tap(None,*self.login_bonus_close_btn,1).perform()
                    time.sleep(2)
                    self.driver.find_element(by=AppiumBy.IMAGE, value=login_bonus_img)
                except:
                    break
        except:
            print("Página de login bonus no encontrada, buscando tablon de anuncios")
            try:
                short_wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=announcements_board_img))
                print("Tablon de anuncios encontrada...")
                time.sleep(2)
                TouchAction(self.driver).tap(None,*self.announcements_board_close_btn,1).perform()
                time.sleep(2)
            except:
                print("Tablon de anuncios no encontrado, buscando anuncios de eventos")                
                try:
                    short_wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=announcement_close_btn_img))
                    print("Anuncio de evento encontrado...")
                    while True:
                        try:
                            print("Cerrando anuncio de evento")
                            TouchAction(self.driver).tap(None,*self.announcement_close_btn,1).perform()
                            time.sleep(2)
                            self.driver.find_element(by=AppiumBy.IMAGE, value=announcement_close_btn_img)
                        except:
                            break
                except:
                    print("No más anuncios.... avanzando a pantalla principal")
        
        print("Buscando pantalla principal")
        self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=main_screen_img))
        print("Pantalla principal encontrada")
        #self.wait.until(EC.or(lambda x: x.find_element(by=AppiumBy.IMAGE, value=close_announcement_btn_img),lambda x: x.find_element(by=AppiumBy.IMAGE, value=main_screen_img)))     

    def get_event_energy(self):
        print("Juntando energia del evento")

        TouchAction(self.driver).tap(None,800, 1430,1).perform()
        time.sleep(2)
        TouchAction(self.driver).tap(None,260, 2140,1).perform()
        time.sleep(2)
        TouchAction(self.driver).tap(None,1200, 1980,1).perform()
        time.sleep(2)
        TouchAction(self.driver).tap(None,800, 1760,1).perform(
)
        
    def start_invasion_mission(self):
        invasion_battle_ends_img = self.load_image("invasion_battle_ends.jpg")
        invasion_main_screen_img = self.load_image("invasion_main_screen.jpg")
        
        
        print("Empezando mision de invasion")
        TouchAction(self.driver).tap(None, *self.main_btn).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None, *self.main_secondary_screen_btn).perform()
        time.sleep(2)
        TouchAction(self.driver).tap(None, *self.main_invasion).perform()
        time.sleep(2)
        for i in range(2):
            self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=invasion_main_screen_img))
            time.sleep(1)
            TouchAction(self.driver).tap(None, *self.invasion_challenge_btn).perform()
            time.sleep(1)
            TouchAction(self.driver).tap(None, *self.invasion_battle_btn).perform()
            time.sleep(30)
            self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=invasion_battle_ends_img))
            time.sleep(2)
            TouchAction(self.driver).tap(None, *self.invasion_battle_ends_confirm).perform()
            time.sleep(5)
        TouchAction(self.driver).tap(None, *self.invasion_goback_btn).perform()
        time.sleep(2)
        #TouchAction(self.driver).tap(None, *self.main_primary_screen_btn).perform()
        #time.sleep(2)
            
    def arena_battles(self):
        arena_main_screen_img = self.load_image("arena_main_screen.jpg")

        print("Empezando batallas en la arena")
        TouchAction(self.driver).tap(None,*self.main_btn).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,*self.main_arena).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,*self.arena_mode_arena).perform()
        time.sleep(1)
        self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=arena_main_screen_img))
        time.sleep(1)
        TouchAction(self.driver).tap(None,*self.arena_choose_opponent).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,800, 2200).perform()
        time.sleep(30)

        self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=self.load_image("arena_battle_finished.jpg")))
        time.sleep(2)
        TouchAction(self.driver).tap(None, 800, 2300).perform()
        time.sleep(1)
        self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=arena_main_screen_img))
        time.sleep(1)

    def get_resources_arena(self):
        arena_main_screen_img = self.load_image("arena_main_screen.jpg")
        print("Juntando recursos arena diarios")
        TouchAction(self.driver).tap(None, *self.main_btn).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,370, 1700).perform()  #Click Arena
        time.sleep(1)
        TouchAction(self.driver).tap(None,500, 1200).perform()   #Select Arena
        time.sleep(1)
        self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=arena_main_screen_img)) #Wait until arena main screen is shown
        time.sleep(1)
        TouchAction(self.driver).tap(None,1100, 2200).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,350, 850).perform()
        time.sleep(1)
        for i in range(4):
            TouchAction(self.driver).tap(None,1220, 1700).perform()      #Boton de selección Confirm purchase
            time.sleep(1)
        TouchAction(self.driver).tap(None,1100, 2070).perform()          #Boton seleccionar compra
        time.sleep(1)
        TouchAction(self.driver).tap(None, 200, 2450).perform()
        time.sleep(2)
    
    def grand_arena_battles(self, number_of_battles):
        g_arena_main_screen_img = self.load_image("g_arena_main_screen.jpg")
        g_arena_battle_ends_img = self.load_image("g_arena_battle_ends.jpg")

        print("Empezando batallas en grand arena")
        TouchAction(self.driver).tap(None,*self.main_btn).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,*self.main_arena).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None, *self.arena_mode_g_arena).perform()
        time.sleep(1)
        self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=g_arena_main_screen_img))
        time.sleep(2)
        TouchAction(self.driver).tap(None, *self.g_arena_reward).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None, *self.g_arena_reward_claim).perform()
        time.sleep(3)
        TouchAction(self.driver).tap(None, *self.g_arena_reward_close).perform()
        time.sleep(1)
        for i in range(number_of_battles):
            TouchAction(self.driver).tap(None, *self.g_arena_choose_opponent).perform()
            time.sleep(1)
            TouchAction(self.driver).tap(None, *self.g_arena_opponent_free).perform()
            time.sleep(2)
            for i in range(3):
                TouchAction(self.driver).tap(None, *self.g_arena_next_team).perform()
                time.sleep(1)
            time.sleep(60)
            self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=g_arena_battle_ends_img))
            time.sleep(2)
            TouchAction(self.driver).tap(None, *self.g_arena_battle_finish_confirm).perform()
            time.sleep(3)
            self.wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=g_arena_main_screen_img))
            time.sleep(2)
        TouchAction(self.driver).tap(None, *self.g_arena_go_back_btn).perform()
        time.sleep(1)

    def get_resources_fragments(self):
        print("Juntando fragmentos de evolución")
        TouchAction(self.driver).tap(None,620, 2430).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,830, 1950).perform()
        time.sleep(1)
        self.driver.swipe(800,2100,800,700,2000)
        time.sleep(1)
        TouchAction(self.driver).tap(None,330, 1230).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,1220, 1700).perform()      #Boton de selección Confirm purchase
        time.sleep(1)
        TouchAction(self.driver).tap(None,1100, 2070).perform()          #Boton seleccionar compra
        time.sleep(1)
        
        TouchAction(self.driver).tap(None,800, 1230).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,1220, 1700).perform()      #Boton de selección Confirm purchase
        time.sleep(1)
        TouchAction(self.driver).tap(None,1100, 2070).perform()          #Boton seleccionar compra
        time.sleep(1)
        
        TouchAction(self.driver).tap(None,1250, 1230).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,1220, 1700).perform()      #Boton de selección Confirm purchase
        time.sleep(1)
        TouchAction(self.driver).tap(None,1100, 2070).perform()          #Boton seleccionar compra
        time.sleep(1)
        
        TouchAction(self.driver).tap(None,330, 1830).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None,1220, 1700).perform()      #Boton de selección Confirm purchase
        time.sleep(1)
        TouchAction(self.driver).tap(None,1100, 2070).perform()          #Boton seleccionar compra
        time.sleep(1)
        
        TouchAction(self.driver).tap(None, 200, 2450).perform()
        time.sleep(2)

    def get_resources_daily_missions(self):
        print("Empezando la recolección de energia y monedas")
        TouchAction(self.driver).tap(None, *self.main_btn).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(None, *self.main_portal).perform()
        time.sleep(1)
        self.driver.swipe(*self.portal_swipe_down)
        time.sleep(1)
        self.driver.swipe(*self.portal_swipe_up)
        time.sleep(1)
        for mission in (self.portal_energy_mission, self.portal_coins_mission):
            TouchAction(self.driver).tap(None, *mission).perform()
            time.sleep(1)
            TouchAction(self.driver).tap(None, *self.portal_choose_mision).perform()
            time.sleep(1)
            TouchAction(self.driver).tap(None, *self.portal_mision_option_sweep).perform()
            time.sleep(1)
            TouchAction(self.driver).tap(None, *self.portal_mission_max_btn).perform()
            time.sleep(1)
            TouchAction(self.driver).tap(None, *self.portal_mission_sweep_btn).perform()
            time.sleep(2)
            TouchAction(self.driver).tap(None, *self.portal_mission_close_btn).perform()
            time.sleep(1)
            TouchAction(self.driver).tap(None, *self.portal_mission_goback).perform()
            time.sleep(1)
        
    def close_game(self, package_name):
        self.driver.terminate_app(package_name)
        self.driver.quit()