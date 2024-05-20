""" trigger/02020028_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=24120001, illust_id='Neirin_normal', msg='$02020028_BF__main__0$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=24120001, illust_id='Neirin_normal', msg='$02020028_BF__main__1$', duration=5000, align=Align.Left)


initial_state = 전투시작
