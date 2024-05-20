""" trigger/02000242_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[701,702])
        self.destroy_monster(spawn_ids=[631,632,633,634,635,636,637,638,639])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[201]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[631,632,633,634,635,636,637,638,639], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[631,632,633,634,635,636,637,638,639]):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520])


initial_state = 대기
