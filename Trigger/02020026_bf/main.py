""" trigger/02020026_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=24110001, illust_id='Neirin_normal', msg='$02020026_BF__main__0$', duration=5000, align=Align.left)
        self.add_cinematic_talk(npc_id=24110001, illust_id='Neirin_normal', msg='$02020026_BF__main__1$', duration=5000, align=Align.left)
        self.add_cinematic_talk(npc_id=24110001, illust_id='Neirin_normal', msg='$02020026_BF__main__2$', duration=5000, align=Align.left)


initial_state = 전투시작
