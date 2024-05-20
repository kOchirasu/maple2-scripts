""" trigger/02020020_bf/02020020_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 카메라_네이린설명1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=24100001, illust_id='Neirin_normal', msg='$02020020_BF__02020020_main__0$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=24100001, illust_id='Neirin_normal', msg='$02020020_BF__02020020_main__1$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=24100001, illust_id='Neirin_normal', msg='$02020020_BF__02020020_main__2$', duration=5000, align=Align.Left)


class 종료(trigger_api.Trigger):
    pass


initial_state = 카메라_네이린설명1
