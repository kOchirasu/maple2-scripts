""" trigger/99999922/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=99999)
        self.set_effect(trigger_ids=[100000001]) # wall01 사라짐
        self.set_effect(trigger_ids=[100000002]) # 다리 생성
        self.set_effect(trigger_ids=[100000003]) # 다리 제거
        self.set_effect(trigger_ids=[100000004]) # wall01 사라짐
        self.set_effect(trigger_ids=[100000005]) # 다리 생성
        self.set_effect(trigger_ids=[100000006]) # 다리 제거
        self.set_mesh(trigger_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008], visible=True)
        self.set_mesh(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111])
        self.set_mesh(trigger_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211])
        self.set_mesh(trigger_ids=[1300,1301,1302,1303,1304,1305,1306,1307,1308], visible=True)
        self.set_mesh(trigger_ids=[1400], visible=True)
        self.set_mesh(trigger_ids=[1500], visible=True)
        self.set_agent(trigger_ids=[1000001,1000002,1000003,1000004,1000005,1000006])
        self.set_agent(trigger_ids=[1100001,1100002,1100003])
        self.set_interact_object(trigger_ids=[10000065], state=2)
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1]):
            return 생성_1(self.ctx)


class 생성_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_1(self.ctx)


class 연출시작_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=2000001)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대화_1(self.ctx)


class 대화_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=101, script='신입사원인가요?', time=5)
        self.set_skip(state=대화_1_스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대화_1_스킵(self.ctx)


class 대화_1_스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대화_2(self.ctx)


class 대화_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=101, script='반가워요.\\n그럼 저를 따라와 보시겠어요??', time=3)
        self.set_skip(state=연출끝_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대화_2_스킵(self.ctx)


class 대화_2_스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출끝_1(self.ctx)


class 연출끝_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=2000001, enable=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 돌사운드_1(self.ctx)

    def on_exit(self) -> None:
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData0_101_1')
        self.set_mesh(trigger_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008], start_delay=2000, interval=100)
        self.set_mesh(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111], visible=True, start_delay=5000, interval=100)


class 돌사운드_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='자경대장 오스칼과 함께 몬스터들을 처치하세요.', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다리사운드_1(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[100000001], visible=True) # wall01 사라짐


class 다리사운드_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 몬스터등장_1(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[100000002], visible=True) # 다리 생성


class 몬스터등장_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1400], start_delay=1000)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저감지_2(self.ctx)


class 유저감지_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2], job_code=0):
            return 길막추가_1(self.ctx)


class 길막추가_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[1000001,1000002,1000003,1000004,1000005,1000006], visible=True)
        self.set_mesh(trigger_ids=[1400], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return npc감지_1(self.ctx)


class npc감지_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2], job_code=0) and self.npc_detected(box_id=2, spawn_ids=[101]):
            return 다리제거_1(self.ctx)


class 다리제거_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111], start_delay=100, interval=100)
        self.set_effect(trigger_ids=[100000003], visible=True) # 다리 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 몬스터사망_1(self.ctx)


class 몬스터사망_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1001]):
            return 번째구역통로오픈3(self.ctx)

    def on_exit(self) -> None:
        self.set_event_ui(type=1, arg2='다리를 건너 마지막 몬스터를 처치하세요!', arg3='4000')


class 번째구역통로오픈3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[1000001,1000002,1000003,1000004,1000005,1000006])
        self.set_mesh(trigger_ids=[1300,1301,1302,1303,1304,1305,1306,1307,1308], start_delay=2000, interval=100)
        self.set_mesh(trigger_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211], visible=True, start_delay=4000, interval=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 돌사운드_2(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[1500], start_delay=5000)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData0_101_2')


class 돌사운드_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1800):
            return 다리사운드_2(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[100000004], visible=True) # wall01 사라짐


class 다리사운드_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1900):
            return 유저감지_3(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[100000005], visible=True) # 다리 생성


class 유저감지_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[3], job_code=0) and self.npc_detected(box_id=3, spawn_ids=[101]):
            return 길막추가_2(self.ctx)


class 길막추가_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1500], visible=True)
        self.set_agent(trigger_ids=[1100001,1100002,1100003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 다리제거_2(self.ctx)


class 다리제거_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=99999, enable=True)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.set_mesh(trigger_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211], start_delay=100, interval=100)
        self.set_effect(trigger_ids=[100000006], visible=True) # 다리 제거

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 몬스터사망_2(self.ctx)


class 몬스터사망_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1002]):
            return 연출시작_2(self.ctx)


class 연출시작_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=99999)
        self.select_camera(trigger_id=2000002)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 레버생성_1(self.ctx)


class 레버생성_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000065], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 대화_3(self.ctx)


class 대화_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=101, script='저 스위치를 당겨야해요!', time=5)
        self.set_skip(state=대화_3_스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대화_3_스킵(self.ctx)


class 대화_3_스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출끝_2(self.ctx)


class 연출끝_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=2000002, enable=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 레버생성_1_완료(self.ctx)

    def on_exit(self) -> None:
        self.set_event_ui(type=1, arg2='생성된 스위치를 작동시키세요!', arg3='4000')


class 레버생성_1_완료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000065], state=0):
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return NPC이동_2(self.ctx)


class NPC이동_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData0_101_3')
        self.set_dialogue(type=1, spawn_id=101, script='오예~끝났당~', time=3, arg5=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return npc감지_4(self.ctx)


class npc감지_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=4, spawn_ids=[101]):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            pass


initial_state = 대기
