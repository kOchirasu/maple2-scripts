""" trigger/52020024_qd/52020024_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='TimerStart', value=0)
        self.set_user_value(trigger_id=99990003, key='FinalPhase', value=0)
        self.set_effect(trigger_ids=[5001])
        self.set_actor(trigger_id=10001, visible=True, initial_sequence='ks_quest_movewall_A02_off')
        self.set_actor(trigger_id=10002, visible=True, initial_sequence='ks_quest_movewall_A02_off')
        self.set_actor(trigger_id=10003, visible=True, initial_sequence='ks_quest_fusiondevice_A01_off')
        self.set_mesh(trigger_ids=[1001], visible=True)
        self.set_mesh(trigger_ids=[2001], visible=True)
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.set_interact_object(trigger_ids=[10002006], state=2)
        self.set_interact_object(trigger_ids=[10002007], state=2)
        self.set_interact_object(trigger_ids=[10002008], state=2)
        self.set_interact_object(trigger_ids=[10002009], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 차전투감지1(self.ctx)


class 차전투감지1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 차전투1(self.ctx)


class 차전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='방 안을 수색하세요', duration=5000, box_ids=['0'])
        self.spawn_monster(spawn_ids=[101,102,103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103], auto_target=False):
            return 번레버활성화1(self.ctx)


class 번레버활성화1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002006], state=1)
        self.add_balloon_talk(msg='파편 융합 장치 전원을 찾아야해', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002006], state=0):
            return 차전투감지2(self.ctx)


class 차전투감지2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1001], start_delay=500)
        self.set_actor(trigger_id=10001, visible=True, initial_sequence='ks_quest_movewall_A02_start')
        self.add_balloon_talk(msg='헐... 대박...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 차전투2(self.ctx)


class 차전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111,112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112], auto_target=False):
            return 번레버활성화2(self.ctx)


class 번레버활성화2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='여기엔 없는것 같네', duration=3000)
        self.set_interact_object(trigger_ids=[10002007], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002007], state=0):
            return 차전투감지3(self.ctx)


class 차전투감지3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001], start_delay=500)
        self.set_actor(trigger_id=10002, visible=True, initial_sequence='ks_quest_movewall_A02_start')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[904]):
            return 차전투3(self.ctx)


class 차전투3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[121,122])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121,122], auto_target=False):
            return 번레버활성화3(self.ctx)


class 번레버활성화3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002008], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002008], state=0):
            return 파편모으기(self.ctx)


class 파편모으기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002009], state=1)
        self.add_balloon_talk(msg='중앙으로 가보자!', duration=3000)
        self.set_event_ui_script(type=BannerType.Text, script='융합장치 전원 활성화.', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002009], state=0):
            return 파이널전투(self.ctx)


class 파이널전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=10003, visible=True, initial_sequence='ks_quest_fusiondevice_A01_on')
        self.set_user_value(trigger_id=99990002, key='TimerStart', value=1)
        self.set_user_value(trigger_id=99990003, key='FinalPhase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart') == 2:
            return 파편합성완료(self.ctx)
        if self.user_value(key='FinalPhase') == 2:
            return 파편합성완료(self.ctx)


class 파편합성완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=10003, visible=True, initial_sequence='ks_quest_fusiondevice_A01_off')
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라_미카엘등장(self.ctx)


class 카메라_미카엘등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(map_id=52020024, portal_id=2)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_Michael')
        self.select_camera(trigger_id=501)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라_미카엘대사1(self.ctx)


class 카메라_미카엘대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='아주 좋아!', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카메라_미카엘대사2(self.ctx)


class 카메라_미카엘대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.set_dialogue(type=1, spawn_id=201, script='파편이 어쩌구~ 저쩌구~', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카메라_지진사태(self.ctx)


class 카메라_지진사태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=503)
        self.set_dialogue(type=1, script='왜...왜 이러지?', time=4)
        self.set_onetime_effect(id=1, enable=True, path='BG\\Common\\Eff_Com_Vibrate_Lowamp.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_바닥부서짐(self.ctx)


class 카메라_바닥부서짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='으아아악!!!', time=2)
        self.select_camera(trigger_id=504)
        self.set_skill(trigger_ids=[1], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020025, portal_id=1)


initial_state = 감지
