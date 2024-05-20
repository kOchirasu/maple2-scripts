""" trigger/02020144_bf/_main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=1003, skill_id=70002151, is_player=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1002]):
            return 보스전_시작(self.ctx)


class 보스전_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__0$', duration=5670, voice='ko/Npc/00002206')
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5670):
            return 조건추가(self.ctx)


class 조건추가(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 보스전_성공(self.ctx)


class 보스전_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(type='trigger', achieve='ClearGreenLapenta_Quest')
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.side_npc_talk(npc_id=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__1$', duration=7940, voice='ko/Npc/00002207')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7940):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        # self.set_achievement(type='trigger', achieve='ClearGreenLapenta')
        # self.remove_buff(box_id=1003, skill_id=70002151, is_player=True)
        # self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
