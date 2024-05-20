""" trigger/02020024_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=23200084, illust_id='Neirin_normal', msg='$02020024_BF__main__0$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=23200084, illust_id='Neirin_normal', msg='$02020024_BF__main__1$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=23200084, illust_id='Neirin_normal', msg='$02020024_BF__main__2$', duration=5000, align=Align.Left)


class 종료(trigger_api.Trigger):
    pass


initial_state = 전투시작
