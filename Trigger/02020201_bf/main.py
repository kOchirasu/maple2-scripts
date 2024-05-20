""" trigger/02020201_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=103)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 페이카등장(self.ctx)


class 페이카등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 페이카 등장
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020201_BF__MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            # 페이카 죽음
            return 제단파괴(self.ctx)


class 제단파괴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020201_BF__MAIN__1$')
        self.add_balloon_talk(spawn_id=101, msg='$02020201_BF__MAIN__2$', duration=3000)
        self.destroy_monster(spawn_ids=[201,202,203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(type='trigger', achieve='PaikaKritiasClear')
        self.dungeon_clear()
        self.set_portal(portal_id=103, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
