""" trigger/52100303_qd/sidetalk.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Sidetalk') == 1:
            self.side_npc_talk(npc_id=11004715, illust='Eone_serious', script='$52100303_QD__SIDETALK__0$', duration=3000)
            return 세번째(self.ctx)


class 세번째(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Sidetalk') == 2:
            self.side_npc_talk(npc_id=11004715, illust='Eone_serious', script='$52100303_QD__SIDETALK__1$', duration=3000)
            return 네번째(self.ctx)


class 네번째(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Sidetalk') == 3:
            self.side_npc_talk(npc_id=11004715, illust='Eone_serious', script='$52100303_QD__SIDETALK__2$', duration=3000)
            return 대사대기(self.ctx)


class 대사대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 계속(self.ctx)


class 계속(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[101]):
            self.side_npc_talk(npc_id=11004715, illust='Eone_serious', script='$52100303_QD__SIDETALK__3$', duration=3000)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
