""" trigger/63000074_cs/63000074_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.set_mesh(trigger_ids=[4001], visible=True) # 루돌프켜기
        self.set_mesh(trigger_ids=[4002], visible=True) # 화분켜기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000370], quest_states=[2]):
            # 해피빌리지(63000072)로 유저 강제이동
            return moveto63000072(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000370], quest_states=[1]):
            return Diary_ready(self.ctx) # 프롤로그 연출
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[30000370], quest_states=[1]):
            return scene_fin(self.ctx) # 연출 종료


class Diary_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불끄기
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Diary_set(self.ctx)


class Diary_set(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_mesh(trigger_ids=[4001]) # 루돌프끄기
        self.set_mesh(trigger_ids=[4002]) # 화분끄기
        self.move_user(map_id=63000074, portal_id=10)
        self.select_camera(trigger_id=8000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Diary_start(self.ctx)


class Diary_start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=sceneskip_1, action='exit') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set
        self.set_cinematic_ui(type=9, script='$63000074_CS__63000074_MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return Evelyn_monologue_00(self.ctx)


class Evelyn_monologue_00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Evelyn_monologue_01(self.ctx)


class Evelyn_monologue_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # 아~ 정말. 맘에 드는 게 하나도 없어.\n어릴 때가 편했는데… 그렇지, 보?
        self.add_cinematic_talk(npc_id=11004354, msg='$63000074_CS__63000074_MAIN__1$', duration=4000, illust_id='Evelyn_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Evelyn_monologue_02(self.ctx)


class Evelyn_monologue_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml') # 불켜기
        self.select_camera_path(path_ids=[8000], return_view=False)
        # …휴. 내가 이상해졌나 봐.\n어린애일 때 찾던 요정 이름이나 부르고.
        self.add_cinematic_talk(npc_id=11004354, msg='$63000074_CS__63000074_MAIN__2$', duration=4000, illust_id='Evelyn_sad', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Evelyn_monologue_03(self.ctx)


class Evelyn_monologue_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        # 하지만… 쓸쓸한걸.\n너라도 있으면, 크리스마스가 슬프진 않을 텐데.
        self.add_cinematic_talk(npc_id=11004354, msg='$63000074_CS__63000074_MAIN__3$', duration=5000, illust_id='Evelyn_sad', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Evelyn_monologue_04(self.ctx)


class Evelyn_monologue_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.add_cinematic_talk(npc_id=11004354, msg='$63000074_CS__63000074_MAIN__4$', duration=3500) # …그만 자야겠다.
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return bobos_ready(self.ctx)


class bobos_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return bobos_01(self.ctx)


class bobos_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 슬프면 안 돼, $npcName:11004345$…\n그런 건 싫어.
        self.set_cinematic_ui(type=9, script='$63000074_CS__63000074_MAIN__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return bobos_02(self.ctx)


class bobos_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004345$ &lt;FONT color='#ffd200'&gt;소원…&lt;/FONT&gt; 들어줄게.\n\n그럼 $npcName:11004345$, 행복해지고\n나는… &lt;FONT color='#ffd200'&gt;루돌프&lt;/FONT&gt;가 될 수 있다.
        self.set_cinematic_ui(type=9, script='$63000074_CS__63000074_MAIN__6$')
        self.set_mesh(trigger_ids=[4001], visible=True) # 루돌프켜기
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return rednose_01(self.ctx)


class rednose_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return rednose_02(self.ctx)


class rednose_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return rednose_03(self.ctx)


class sceneskip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return rednose_03(self.ctx)


class rednose_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9000, type='trigger', achieve='LonelyEvelyn')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return moveto63000072(self.ctx)


class moveto63000072(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000072, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return moveto63000072_2(self.ctx)


class moveto63000072_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000072, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return moveto63000072(self.ctx)


class scene_fin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 준비
