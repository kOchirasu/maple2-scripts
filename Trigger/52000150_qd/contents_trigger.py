""" trigger/52000150_qd/contents_trigger.xml """
import trigger_api


class 차원의숲전경씬종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='52000150') == 1:
            return 웨이브1알림(self.ctx)


# ########################전투 컨텐츠 시작, 웨이브1########################
class 웨이브1알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], visible=True, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[2]):
            # B퀘스트가 진행 중 일때
            return 컨텐츠종료01(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 웨이브1생성(self.ctx)


class 웨이브1생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[400,401,402,403,404]):
            return 웨이브2알림(self.ctx)


# #######################웨이브2########################
class 웨이브2알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 웨이브2생성(self.ctx)


class 웨이브2생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500,501,502,503,504], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[500,501,502,503,504]):
            return 웨이브3알림(self.ctx)


# ########################웨이브3########################
class 웨이브3알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 웨이브3생성(self.ctx)


class 웨이브3생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[600,601,602,603,604], auto_target=False)
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[600,601,602,603,604]):
            return 웨이브4알림(self.ctx)


# ########################웨이브4########################
class 웨이브4알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 웨이브4생성(self.ctx)


class 웨이브4생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[300,301,302,303,304], auto_target=False)
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[300,301,302,303,304]):
            return 웨이브5알림(self.ctx)


# ########################웨이브5, 1번/3번지역 동시 등장########################
class 웨이브5알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], visible=True, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 웨이브5생성(self.ctx)


class 웨이브5생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[600,601,602,603,604], auto_target=False)
        self.spawn_monster(spawn_ids=[400,401,402,403,404], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[600,601,602,603,604,400,401,402,403,404]):
            return 웨이브6알림(self.ctx)


# ########################웨이브6, 2번/4번지역 동시 등장########################
class 웨이브6알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 웨이브6생성(self.ctx)


class 웨이브6생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500,501,502,503,504], auto_target=False)
        self.spawn_monster(spawn_ids=[300,301,302,303,304], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[300,301,302,303,304,500,501,502,503,504]):
            return 웨이브7알림(self.ctx)


# ########################웨이브7, 전 지역 동시 등장########################
class 웨이브7알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], visible=True, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 웨이브7생성(self.ctx)


class 웨이브7생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[300,301,302,303,304], auto_target=False)
        self.spawn_monster(spawn_ids=[400,401,402,403,404], auto_target=False)
        self.spawn_monster(spawn_ids=[500,501,502,503,504], auto_target=False)
        self.spawn_monster(spawn_ids=[600,601,602,603,604], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[300,301,302,303,304,400,401,402,403,404,500,501,502,503,504,600,601,602,603,604]):
            return 컨텐츠종료01(self.ctx)


# ########################컨텐츠종료01########################
class 컨텐츠종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[300,301,302,303,304,400,401,402,403,404,500,501,502,503,504,600,601,602,603,604])
        self.set_cinematic_ui(type=1)
        self.set_time_scale(enable=True, start_scale=0.1, end_scale=0.5, duration=10.0, interpolator=1) # 2초간 느려지기 시작
        # self.set_achievement(trigger_id=10010, type='trigger', achieve='ProtectFinish')
        # self.set_user_value(trigger_id=10000, key='52000150monster', value=1) # 통신 : 몬스터 다 잡으면 쏴주는 신호

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 컨텐츠종료02(self.ctx)


class 컨텐츠종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_effect(trigger_ids=[2607])
        self.destroy_monster(spawn_ids=[700])
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_caitMove01') # 케이틀린 이동
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_A') # 호르헤
        self.set_npc_emotion_loop(spawn_id=200, sequence_name='Event_01_A', duration=999999.0)
        self.set_user_value(trigger_id=10000, key='52000150monster', value=1) # 통신 : 몬스터 다 잡으면 쏴주는 신호

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 컨텐츠종료03(self.ctx)


class 컨텐츠종료03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        # self.set_cinematic_ui(type=0)
        # self.set_cinematic_ui(type=2)
        self.set_user_value(trigger_id=10000, key='52000150monster', value=0)


initial_state = 차원의숲전경씬종료
