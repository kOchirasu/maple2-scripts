""" trigger/61000002_me_002/massive01.xml """
import trigger_api


# 파이널서바이버
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 퍼즐대기중(self.ctx)


class 퍼즐대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211], visible=True)
        self.set_actor(trigger_id=251, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=252, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=253, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=254, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=255, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=256, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=257, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=258, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=259, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=260, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=261, visible=True, initial_sequence='Eff_MassiveEvent_Door_Opened')
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_portal(portal_id=777, enable=True)
        self.set_portal(portal_id=778, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=779, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=301) >= 50:
            return 계단없애기(self.ctx)
        if self.wait_tick(wait_tick=60000):
            return 계단없애기(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=261, visible=True, initial_sequence='Eff_MassiveEvent_Door_Vanished')
        self.set_portal(portal_id=777)


class 계단없애기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=301) # 해킹 보안용 시작 box 설정
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 계단없애기2(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[206,207,208,209,210,211])
        self.set_actor(trigger_id=256, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=257, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=258, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=259, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=260, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=261, initial_sequence='Eff_MassiveEvent_Door_Vanished')
        self.reset_timer(timer_id='1')


class 계단없애기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[201,202,203,204,205])
        self.set_actor(trigger_id=251, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=252, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=253, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=254, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=255, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=256, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=257, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=258, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=259, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=260, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.reset_timer(timer_id='1')


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트0(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.play_system_sound_in_box(sound='ME_002_Massive01_00')
        # 로그에서 해당 이벤트에 참여한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__0$', arg3='6000')
        # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        self.start_mini_game(box_id=301, round=4, game_name='finalsurvivor')
        self.set_achievement(trigger_id=301, type='trigger', achieve='finalsurvivor_start')
        # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        self.set_achievement(trigger_id=301, type='trigger', achieve='dailyquest_start')
        self.give_guild_exp(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트1(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=11)
        self.play_system_sound_in_box(sound='ME_002_Massive01_01')
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__1$', arg3='11000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=9)
        self.play_system_sound_in_box(sound='ME_002_Massive01_02')
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__2$', arg3='9000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트3(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)
        self.set_event_ui(type=0, arg2='1,4')
        self.show_count_ui(text='$61000002_ME_002__MASSIVE01__3$', stage=1, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계1대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=301, round=1)
        self.set_timer(timer_id='1', seconds=40)
        self.set_random_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], start_delay=20, fade=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계1정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=301, exp_rate=0.25)
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1정리2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계1정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            self.set_event_ui(type=0, arg2='2,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__4$', stage=2, count=5)
            return 퍼즐단계2대기(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 실패(self.ctx)


class 퍼즐단계2대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=301, round=2)
        self.set_timer(timer_id='1', seconds=30)
        self.set_random_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], start_delay=30, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계2정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계2정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=301, exp_rate=0.25)
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계2정리2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계2정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            self.set_event_ui(type=0, arg2='3,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__5$', stage=3, count=5)
            return 퍼즐단계3대기(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 실패(self.ctx)


class 퍼즐단계3대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계3(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=301, round=3)
        self.set_timer(timer_id='1', seconds=15)
        self.set_random_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], start_delay=30, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계3정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계3정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=301, exp_rate=0.25)
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계3정리2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계3정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            self.set_event_ui(type=0, arg2='4,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__6$', stage=4, count=5)
            return 퍼즐단계4대기(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 실패(self.ctx)


class 퍼즐단계4대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계4(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_mini_game_round(box_id=301, round=4)
        self.set_timer(timer_id='1', seconds=5)
        self.set_random_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], start_delay=15, fade=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계4정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계4정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=301, exp_rate=0.25)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계4정리2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계4정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
            return 우승자카메라연출(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 실패(self.ctx)


class 우승자카메라연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.mini_game_camera_direction(box_id=301, camera_id=901)
        self.set_event_ui(type=0, arg2='0,0')
        self.play_system_sound_in_box(sound='ME_002_Massive01_07')
        self.set_event_ui(type=3, arg2='$61000002_ME_002__MASSIVE01__7$', arg3='7000', arg4='301')
        self.set_event_ui(type=6, arg2='$61000002_ME_002__MASSIVE01__8$', arg3='7000', arg4='!301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_local_camera(camera_id=901)
            return 보상단계(self.ctx)


class 보상단계(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[301], sound='ME_001_Massive00_10')
        self.set_event_ui(type=3, arg2='$61000002_ME_002__MASSIVE01__9$', arg3='5000', arg4='301')
        self.set_event_ui(type=6, arg2='$61000002_ME_002__MASSIVE01__10$', arg3='5000', arg4='!301')
        # 로그에서 해당 이벤트에서 우승한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        self.add_buff(box_ids=[301], skill_id=70000019, level=1)
        self.mini_game_give_reward(winner_box_id=301, content_type='miniGame')
        # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        self.end_mini_game(winner_box_id=301, game_name='finalsurvivor')
        self.set_achievement(trigger_id=301, type='trigger', achieve='finalsurvivor_win')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퍼즐종료계단보이기(self.ctx)


class 퍼즐종료계단보이기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='0,0')
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_mesh(trigger_ids=[201,202,203,204,205], visible=True)
        self.set_actor(trigger_id=251, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=252, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=253, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=254, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=255, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐종료계단보이기2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐종료계단보이기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[206,207,208,209,210], visible=True)
        self.set_actor(trigger_id=256, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=257, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=258, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=259, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=260, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐종료(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[211], visible=True)
        self.set_actor(trigger_id=261, visible=True, initial_sequence='Eff_MassiveEvent_Door_Opened')
        self.reset_timer(timer_id='1')


class 퍼즐종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_event_ui(type=0, arg2='0,0')
        self.set_portal(portal_id=777, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저이동(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.end_mini_game_round(winner_box_id=301)
        self.end_mini_game(winner_box_id=301, game_name='finalsurvivor')
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_event_ui(type=0, arg2='0,0')
        self.play_system_sound_in_box(box_ids=[301], sound='ME_001_Massive00_14')
        self.set_event_ui(type=5, arg2='$61000002_ME_002__MASSIVE01__13$', arg3='5000')
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_portal(portal_id=777, enable=True)
        self.set_mesh(trigger_ids=[201,202,203,204,205], visible=True)
        self.set_actor(trigger_id=251, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=252, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=253, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=254, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=255, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 실패계단보이기2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 실패계단보이기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[206,207,208,209,210], visible=True)
        self.set_actor(trigger_id=256, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=257, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=258, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=259, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=260, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 유저이동(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[211], visible=True)
        self.set_actor(trigger_id=261, visible=True, initial_sequence='Eff_MassiveEvent_Door_Opened')
        self.reset_timer(timer_id='1')


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__23$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=120000):
            self.move_user()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
