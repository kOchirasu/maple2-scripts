""" trigger/02000298_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000004], state=2)
        self.set_effect(trigger_ids=[601])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005], visible=True)
        self.set_mesh(trigger_ids=[3221,3222,3223])
        self.spawn_monster(spawn_ids=[2099], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=2099, sequence_name='Idle_A', duration=9999999.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=암호발급)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=300)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라이동후UI노출(self.ctx)


class 카메라이동후UI노출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.show_guide_summary(entity_id=20002991, text_id=20002991, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2099, patrol_name='MS2PatrolData_2099_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 던전안내01(self.ctx)


class 던전안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3221,3222,3223], visible=True)
        self.set_interact_object(trigger_ids=[10000372], state=1)
        self.show_guide_summary(entity_id=20002980, text_id=20002980, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera(trigger_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 던전안내카메라이동(self.ctx)


class 던전안내카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 던전안내02(self.ctx)


class 던전안내02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002981, text_id=20002981, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_interact_object(trigger_ids=[10000372], state=0)
            return 암호발급(self.ctx)


class 암호발급(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=199, skill_id=70000107)
        self.destroy_monster(spawn_ids=[2099])
        self.select_camera(trigger_id=302, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005], fade=5.0)
        self.set_mesh(trigger_ids=[3221,3222,3223], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return 소환1279(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환1238(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환1358(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환1489(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환1567(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환1679(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환2389(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환2347(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환2478(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환2456(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환2569(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환2678(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3458(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3589(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3679(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3789(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환4567(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환4578(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환4689(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환4789(self.ctx)


class 소환1279(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[1279], auto_target=False)
        return 종료(self.ctx)


class 소환1238(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[1238], auto_target=False)
        return 종료(self.ctx)


class 소환1358(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[1358], auto_target=False)
        return 종료(self.ctx)


class 소환1489(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[1489], auto_target=False)
        return 종료(self.ctx)


class 소환1567(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[1567], auto_target=False)
        return 종료(self.ctx)


class 소환1679(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[1679], auto_target=False)
        return 종료(self.ctx)


class 소환2389(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[2389], auto_target=False)
        return 종료(self.ctx)


class 소환2347(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[2347], auto_target=False)
        return 종료(self.ctx)


class 소환2478(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[2478], auto_target=False)
        return 종료(self.ctx)


class 소환2456(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[2456], auto_target=False)
        return 종료(self.ctx)


class 소환2569(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[2569], auto_target=False)
        return 종료(self.ctx)


class 소환2678(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[2678], auto_target=False)
        return 종료(self.ctx)


class 소환3458(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[3458], auto_target=False)
        return 종료(self.ctx)


class 소환3589(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[3589], auto_target=False)
        return 종료(self.ctx)


class 소환3679(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[3679], auto_target=False)
        return 종료(self.ctx)


class 소환3789(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[3789], auto_target=False)
        return 종료(self.ctx)


class 소환4567(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[4567], auto_target=False)
        return 종료(self.ctx)


class 소환4578(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[4578], auto_target=False)
        return 종료(self.ctx)


class 소환4689(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[4689], auto_target=False)
        return 종료(self.ctx)


class 소환4789(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.spawn_monster(spawn_ids=[4789], auto_target=False)
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
