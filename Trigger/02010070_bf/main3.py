""" trigger/02010070_bf/main3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163])
        self.set_mesh(trigger_ids=[164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219])
        self.set_mesh(trigger_ids=[300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363])
        self.set_mesh(trigger_ids=[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428])
        self.set_mesh(trigger_ids=[430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460])
        self.set_mesh(trigger_ids=[470,471,472,473,474,475,476,477,478,479,480,481])
        self.set_mesh(trigger_ids=[490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508])
        self.set_mesh(trigger_ids=[220,221,222,223])
        self.destroy_monster(spawn_ids=[3000])
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=9, visible=True, enable=True)
        self.set_effect(trigger_ids=[9000])
        self.set_skill(trigger_ids=[9001])
        self.set_skill(trigger_ids=[9002])
        self.set_skill(trigger_ids=[9003])
        self.set_skill(trigger_ids=[9004])
        self.set_effect(trigger_ids=[95000])
        self.set_effect(trigger_ids=[95003])
        self.set_effect(trigger_ids=[95010])
        self.set_effect(trigger_ids=[95002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999994]):
            return 대기시간안내01(self.ctx)


class 대기시간안내01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기시간안내02(self.ctx)


class 대기시간안내02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 환상을 만든 미치광이 환영술사 카칼프를 처치하세요.
        self.show_guide_summary(entity_id=20100703, text_id=20100703)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작1(self.ctx)


class 시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[3000], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작2(self.ctx)


class 시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20100703)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3000]):
            return 시작3(self.ctx)


class 시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=88321, type='trigger', achieve='kakalfillusion')
        self.set_effect(trigger_ids=[9000], visible=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 사원 가운데 화살표가 있는 곳으로 이동하세요.
        self.show_guide_summary(entity_id=20100704, text_id=20100704)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999995]):
            return 시작35(self.ctx)


class 시작35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2010070, portal_id=11)
        self.set_mesh(trigger_ids=[220,221,222,223], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작4(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163], visible=True)
        self.set_mesh(trigger_ids=[164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219], visible=True)


class 시작4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[9000])
        self.set_skill(trigger_ids=[9001], enable=True)
        self.set_effect(trigger_ids=[95002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 시작5(self.ctx)


class 시작5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20100704)
        self.set_skill(trigger_ids=[9002], enable=True)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28])
        self.set_mesh(trigger_ids=[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
        self.set_mesh(trigger_ids=[50,51,52,53,54,55,56,57,58,59,60,61])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작6(self.ctx)


class 시작6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363], visible=True, interval=50)
        self.set_mesh(trigger_ids=[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428], visible=True, interval=50)
        self.set_mesh(trigger_ids=[430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458], visible=True, interval=50)
        self.set_skill(trigger_ids=[9003], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작7(self.ctx)


class 시작7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481], visible=True, interval=200)
        self.set_mesh(trigger_ids=[490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508], visible=True, interval=200)
        self.set_effect(trigger_ids=[95003], visible=True)
        self.set_skill(trigger_ids=[9004], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 시작8(self.ctx)


class 시작8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208])
        self.set_mesh(trigger_ids=[211,212,213,214,215,216,217,218,219])
        self.set_event_ui(type=1, arg2='$02010070_BF__MAIN__5$', arg3='6000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[220,221,222,223])
        self.set_portal(portal_id=10, visible=True, enable=True)
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return PCGetOut01(self.ctx)


class PCGetOut01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return PCGetOut02(self.ctx)


class PCGetOut02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return PCGetOut03(self.ctx)


class PCGetOut03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return PCGetOut04(self.ctx)


class PCGetOut04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()


initial_state = 대기
