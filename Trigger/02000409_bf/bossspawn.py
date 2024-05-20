""" trigger/02000409_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1,2,3,4,5], visible=True)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[999], auto_target=False) # 이벤트
        self.spawn_monster(spawn_ids=[99], auto_target=False) # 핑크빈
        self.spawn_monster(spawn_ids=[90], auto_target=False)
        self.spawn_monster(spawn_ids=[91], auto_target=False)
        self.spawn_monster(spawn_ids=[92], auto_target=False)
        self.spawn_monster(spawn_ids=[93], auto_target=False)
        self.spawn_monster(spawn_ids=[94], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 종료딜레이(self.ctx)
        if self.dungeon_timeout():
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9999998, key='BattleEnd', value=1)
        self.set_mesh(trigger_ids=[3002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.dungeon_clear()
            return 종료(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_user_value(trigger_id=9999998, key='BattleEnd', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


initial_state = 시작대기중
