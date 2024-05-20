""" trigger/52000091_qd/52000091_trigger.xml """
import trigger_api


class 분기검사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_gravity(gravity=-39.0)
        # self.add_buff(box_ids=[9002], skill_id=70000107, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100570], quest_states=[3]):
            return 로이동52000091(self.ctx) # 오르데 및 다른부대 지휘관들과 합류씬
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100570], quest_states=[2]):
            return 로이동52000091(self.ctx) # 오르데 및 다른부대 지휘관들과 합류씬
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100570], quest_states=[1]):
            # 50100560완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return 로이동52000093(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002282], quest_states=[3]):
            # 20002282완료상태일때, 20002280 퀘스트를 못 받고 나간 애들을 위한 케어
            return 완료가능할때20002282(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100570], quest_states=[1]):
            # 50100560완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return 분기검사02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100560], quest_states=[3]):
            # 50100560완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return None # Missing State: 로이동52000095
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100560], quest_states=[3]):
            # 50100560완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return 분기검사02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100560], quest_states=[1]):
            # 50100560완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return 로이동52000094(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100560], quest_states=[1]):
            # 50100560완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return 분기검사02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100550], quest_states=[3]):
            # 50100550완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return 로이동52000094(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100550], quest_states=[3]):
            # 50100550완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return 분기검사02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[3]):
            # 50100520드디어,하지만 갑자기 퀘스트 완료상태일때, 50100530 퀘스트를 못 받고 나간 애들을 위한 케어
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[3]):
            # 50100520드디어,하지만 갑자기 퀘스트 완료상태일때, 50100530 퀘스트를 못 받고 나간 애들을 위한 케어
            return 분기검사02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[2]):
            # 50100520드디어,하지만 갑자기 퀘스트 진행중일때, 나간 애들을 위한 케어
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[2]):
            # 50100520드디어,하지만 갑자기 퀘스트 진행중일때, 나간 애들을 위한 케어
            return 분기검사02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002282], quest_states=[2]):
            return 완료가능할때20002282(self.ctx) # 오르데 및 다른부대 지휘관들과 합류씬
        if not self.quest_user_detected(box_ids=[9001], quest_ids=[50100570], quest_states=[2]):
            return 분기검사02(self.ctx) # 오르데 및 다른부대 지휘관들과 합류씬
        if not self.quest_user_detected(box_ids=[9001], quest_ids=[20002282], quest_states=[2]):
            return 분기검사02(self.ctx) # 오르데 및 다른부대 지휘관들과 합류씬


class 분기검사02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100570], quest_states=[3]):
            return 로이동52000091(self.ctx) # 오르데 및 다른부대 지휘관들과 합류씬
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100570], quest_states=[2]):
            # 오르데 및 다른부대 지휘관들과 합류씬
            return None # Missing State: 완료가능할때50100570
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100570], quest_states=[1]):
            # 50100560완료상태일때, 공허의 들판으로 못간 애들을 위한 케어
            return 로이동52000093(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100560], quest_states=[2]):
            return 완료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002281], quest_states=[2]):
            return 완료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100560], quest_states=[1]):
            return 완료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002281], quest_states=[1]):
            return 완료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100560], quest_states=[3]):
            return 완료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002281], quest_states=[3]):
            return 완료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100550], quest_states=[2]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002280], quest_states=[2]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100550], quest_states=[1]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002280], quest_states=[1]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100550], quest_states=[3]):
            return 완료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002280], quest_states=[3]):
            return 완료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100540], quest_states=[3]):
            # 20002279완료상태일때, 20002280 퀘스트를 못 받고 나간 애들을 위한 케어
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002279], quest_states=[3]):
            # 20002279완료상태일때, 20002280 퀘스트를 못 받고 나간 애들을 위한 케어
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[2]):
            return 완료가능할때20002277(self.ctx) # 마드리아의 성이 드러나는 연출 시작
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002277], quest_states=[2]):
            return 완료가능할때20002277(self.ctx) # 마드리아의 성이 드러나는 연출 시작
        if not self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[2]):
            return 완료(self.ctx) # 마드리아의 성이 드러나는 연출 시작
        if not self.quest_user_detected(box_ids=[9001], quest_ids=[20002277], quest_states=[2]):
            return 완료(self.ctx) # 마드리아의 성이 드러나는 연출 시작


class 로이동52000094(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000094, portal_id=99)


class 로이동52000093(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000093, portal_id=99)


class 로이동52000091(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_gravity(gravity=-9.8)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52000091, portal_id=99)
        self.spawn_monster(spawn_ids=[200])
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.spawn_npc_range(range_ids=[210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 완료가능할때02_20002282(self.ctx)


class 완료가능할때20002282(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_gravity(gravity=-9.8)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52000091, portal_id=99)
        self.spawn_monster(spawn_ids=[200])
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.spawn_npc_range(range_ids=[210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 완료가능할때02_20002282(self.ctx)


class 완료가능할때02_20002282(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100580], quest_states=[3]):
            return 마드리아쿠키01(self.ctx) # 마드리아 쿠키씬
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002283], quest_states=[3]):
            return 마드리아쿠키01(self.ctx) # 마드리아 쿠키씬


class 마드리아쿠키01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드리아쿠키02(self.ctx)


class 마드리아쿠키02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=90000, enable=True) # 마드리아 고조 브금
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000091_QD__52000091_TRIGGER__0$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드리아쿠키03(self.ctx)


class 마드리아쿠키03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000091_QD__52000091_TRIGGER__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드리아쿠키04(self.ctx)


class 마드리아쿠키04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000091_QD__52000091_TRIGGER__2$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드리아쿠키05(self.ctx)


class 마드리아쿠키05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000091_QD__52000091_TRIGGER__3$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드리아쿠키_끝(self.ctx)


class 마드리아쿠키_끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000402, portal_id=1)


# 디펜스 컨텐츠2로 출발
class 로이동52000099(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000099, portal_id=2)


# 마드리아의 성이 드러나는 연출 시작
class 완료가능할때20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        # self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52000091, portal_id=99)
        self.spawn_monster(spawn_ids=[200])
        self.set_npc_emotion_loop(spawn_id=200, sequence_name='Stun_A', duration=18000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 사운드이펙트(self.ctx)


class 사운드이펙트(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마드라칸연출01(self.ctx)


class 마드라칸연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[1000,1001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드라칸연출02(self.ctx)


class 마드라칸연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1002,1003], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Jump_Damg_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 마드라칸연출03(self.ctx)


class 마드라칸연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1004,1008,1009,1010], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=18000):
            return 마드라칸연출04(self.ctx)


class 마드라칸연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드라칸연출05(self.ctx)


class 마드라칸연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200])


initial_state = 분기검사01
