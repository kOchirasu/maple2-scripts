""" trigger/52000093_qd/20002281_rp.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9100], quest_ids=[50100560], quest_states=[3]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(box_ids=[9100], quest_ids=[20002281], quest_states=[3]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3003,3004])
        self.reset_camera()
        self.set_local_camera(camera_id=302)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=300)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_npc_range(range_ids=[1101,1102,1103,1104,1105,1106])
        self.spawn_npc_range(range_ids=[2101,2102,2103,2104,2105,2106,2107,2108,2109])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 타이틀(self.ctx)


class 타이틀(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000093, portal_id=99)
        self.add_buff(box_ids=[9100], skill_id=99910190, level=1, is_player=False, is_skill_set=False)
        self.set_cinematic_ui(type=9, script='$52000093_QD__20002281_RP__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 오스칼대사01(self.ctx)


class 오스칼대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000093_QD__20002281_RP__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return RP시작(self.ctx)


class RP시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3003,3004], visible=True) # 뒤로 못나가게 한다
        self.select_camera(trigger_id=300, enable=False)
        self.set_local_camera(camera_id=302, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25200931, text_id=25200931, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2101,2102,2103,2104,2105,2106,2107,2108,2109]):
            return 데보라크소환(self.ctx)
        if self.wait_tick(wait_tick=40000):
            return 데보라크소환(self.ctx)


class 데보라크소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[2199], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 데보라크사망대기(self.ctx)


class 데보라크사망대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25200932, text_id=25200932, duration=4000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_local_camera(camera_id=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2199]):
            return 미션완료(self.ctx)


class 미션완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2101,2102,2103,2104,2105,2106,2107,2108,2109])
        self.set_event_ui(type=7, arg2='$52000093_QD__20002281_RP__2$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_local_camera(camera_id=302)
            self.reset_camera()
            return 미션완료02(self.ctx)


class 미션완료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[1100])
        self.remove_buff(box_id=9100, skill_id=99910190)
        self.reset_camera()
        self.set_achievement(trigger_id=9100, type='trigger', achieve='OscalRpClear')
        self.move_user(map_id=52000093, portal_id=99)


initial_state = 대기
