""" trigger/52010032_qd/main_quest10003078.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 무르파고스 신전에 나메드를 만나러 들어오는 퀘스트
class 무르파고스에들어오면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 퀘스트 나메드: 11000039

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003078], quest_states=[2]):
            self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[301]) # 시끄러운 주먹
        self.spawn_monster(spawn_ids=[302]) # 에바고르
        self.move_user(map_id=52010032, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 무르파고스이동(self.ctx)


class 무르파고스이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 무르파고스이동01(self.ctx)


class 무르파고스이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user_path(patrol_name='MS2PatrolData_3005')
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_3003')
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_3004')
        self.show_caption(type='VerticalCaption', title='$52010032_QD__MAIN_QUEST10003078__0$', desc='$52010032_QD__MAIN_QUEST10003078__1$', align=Align.Center | Align.Left, duration=3000, scale=2.0)
        self.add_balloon_talk(spawn_id=301, msg='$52010032_QD__MAIN_QUEST10003078__2$', duration=2000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=302, msg='$52010032_QD__MAIN_QUEST10003078__3$', duration=2000, delay_tick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 나메드에게퀘스트받기(self.ctx)


class 나메드에게퀘스트받기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return None # Missing State: State


initial_state = 무르파고스에들어오면
