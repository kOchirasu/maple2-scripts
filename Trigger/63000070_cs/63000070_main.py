""" trigger/63000070_cs/63000070_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class standby(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=20)
        self.set_mesh(trigger_ids=[529], visible=True)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_interact_object(trigger_ids=[32000015], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return questcheck(self.ctx)


class questcheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000357], quest_states=[2]):
            return gotolobby_ready(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000357], quest_states=[1]):
            return scene1_ready(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000357], quest_states=[3]):
            return emptyroom(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return emptyroom(self.ctx)


class emptyroom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,105,111,112,113,114,115,116,117,118,119,120,201,211,221]) # 연출용 NPC 준비 : 지우기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000357], quest_states=[2]):
            return gotolobby_ready(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000357], quest_states=[1]):
            return scene1_ready(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return scene_fin(self.ctx)


class gotolobby_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,105,111,112,113,114,115,116,117,118,119,120,201,211,221]) # 연출용 NPC 준비 : 지우기
        # 연출용 NPC 준비 : 꼬마유령 마리엔만 생성
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.set_portal(portal_id=20, visible=True, enable=True, minimap_visible=True) # 로비로 이동하는 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[30000357], quest_states=[2]):
            return questcheck(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return scene_fin(self.ctx)


class scene1_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,105,111,112,113,114,115,116,117,118,119,120,201,211,221]) # 연출용 NPC 준비 : 지우기
        self.spawn_monster(spawn_ids=[101,111,112,113,114,115,116,117,118,119,120], auto_target=False) # 연출용 NPC 준비 : 생성
        # 연출용 오브젝트 서류가방 : 반응완료 상태로 만들어 안 보이게 처리
        self.set_interact_object(trigger_ids=[32000015], state=2)
        self.visible_my_pc(is_visible=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[30000357], quest_states=[1]):
            return questcheck(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return scene1_set(self.ctx)


class scene1_set(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return scene1_start(self.ctx)


class scene1_start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000,8001], return_view=False)
        self.set_scene_skip(state=sceneskip_1, action='exit') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set
        # 세상에는 바보들이 참 많아.\n자신들이 할 수 없는 일에 쓸데없이 힘을 쏟는, 그런 바보들 말이야.
        self.add_cinematic_talk(npc_id=11004289, illust_id='Rue_Halloween', msg='$63000070_CS__63000070_MAIN__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene1_ladymonologue1(self.ctx)


class scene1_ladymonologue1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8001,8002], return_view=False)
        self.move_user(map_id=63000070, portal_id=10) # PC, 복도 앞으로 자동 이동
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        # 고아가 된 어린애나,\n유언장을 찾겠다고 나서는 것들이나….
        self.add_cinematic_talk(npc_id=11004289, illust_id='Rue_Halloween', msg='$63000070_CS__63000070_MAIN__1$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene1_ladymonologue2(self.ctx)


class scene1_ladymonologue2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.add_cinematic_talk(npc_id=11004289, illust_id='Rue_Halloween', msg='$63000070_CS__63000070_MAIN__2$', duration=3000) # 뭔가 바꿀 수 있을 거라고 생각해?
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene1_ladyzoomin(self.ctx)


class scene1_ladyzoomin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005,8006], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        # 어리석은 자들!\n아무 것도 바꿀 수 없어!
        self.add_cinematic_talk(npc_id=11004289, msg='$63000070_CS__63000070_MAIN__3$', duration=4000)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Idle_A', duration=4000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene1_ladygoback1(self.ctx)


class scene1_ladygoback1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006,8007], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='Patrol_lady_backward_01')
        # 하지만 여기까지 온 것이 가상하니까,\n제안을 하나 하지.
        self.add_cinematic_talk(npc_id=11004289, illust_id='Rue_Halloween', align=Align.Right, msg='$63000070_CS__63000070_MAIN__4$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene1_ladygoback2(self.ctx)


class scene1_ladygoback2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8008], return_view=False)
        # 자, 네가 원하던 것!\n가질 수 있다면 가져봐.
        self.add_cinematic_talk(npc_id=11004289, illust_id='Rue_Halloween', align=Align.Right, msg='$63000070_CS__63000070_MAIN__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene1_ladygoback3(self.ctx)


class scene1_ladygoback3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='Patrol_lady_backward_02')
        # 그래… 네가 찾으려던 것, 이 안에 있어.\n하지만 넌 얻을 수 없을 거야.
        self.add_cinematic_talk(npc_id=11004289, illust_id='Rue_Halloween', align=Align.Right, msg='$63000070_CS__63000070_MAIN__6$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene1_ladygoback4(self.ctx)


class scene1_ladygoback4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004289, illust_id='Rue_Halloween', align=Align.Right, msg='$63000070_CS__63000070_MAIN__7$', duration=4000) # 왠줄 알아?
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene1_robottroops(self.ctx)


class scene1_robottroops(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8011], return_view=False)
        self.move_npc(spawn_id=111, patrol_name='Patrol_bot_01')
        self.move_npc(spawn_id=112, patrol_name='Patrol_bot_02')
        self.move_npc(spawn_id=113, patrol_name='Patrol_bot_03')
        self.move_npc(spawn_id=114, patrol_name='Patrol_bot_04')
        self.move_npc(spawn_id=115, patrol_name='Patrol_bot_05')
        self.move_npc(spawn_id=116, patrol_name='Patrol_bot_06')
        self.move_npc(spawn_id=117, patrol_name='Patrol_bot_07')
        self.move_npc(spawn_id=118, patrol_name='Patrol_bot_08')
        self.move_npc(spawn_id=119, patrol_name='Patrol_bot_09')
        self.move_npc(spawn_id=120, patrol_name='Patrol_bot_10')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene1_ladygoback5(self.ctx)


class scene1_ladygoback5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='Patrol_lady_backward_03')
        self.add_cinematic_talk(npc_id=11004289, illust_id='Rue_Halloween', align=Align.Center, msg='$63000070_CS__63000070_MAIN__8$', duration=3000) # 그 전에 목숨을 잃게 될 테니까!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene1_readytofight(self.ctx)


class scene1_readytofight(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return scene1_setbattle(self.ctx)


class sceneskip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        self.move_user(map_id=63000070, portal_id=10) # PC, 복도 앞으로 자동 이동
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene1_setbattle(self.ctx)


class scene1_setbattle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,105,111,112,113,114,115,116,117,118,119,120]) # 연출용 NPC 준비 : 지우기
        self.visible_my_pc(is_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene1_setbattle1(self.ctx)


class scene1_setbattle1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='Patrol_PC_fightposition') # 전투하는 곳으로 달려감
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wave_1st_ready(self.ctx)


class wave_1st_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        self.spawn_monster(spawn_ids=[201]) # 몬스터 준비 : 생성
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wave_1st_go(self.ctx)


class wave_1st_go(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201]):
            return wave_2nd_ready(self.ctx)


class wave_2nd_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wave_2nd_go(self.ctx)


class wave_2nd_go(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[211], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[211]):
            return wave_3rd_ready(self.ctx)


class wave_3rd_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wave_3rd_go(self.ctx)


class wave_3rd_go(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[221], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[221]):
            return scene2_marienneappears_ready(self.ctx) # 유령연출 준비


class scene2_marienneappears_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        # NPC,몬스터 남아있을 수 있는 애들 다 지우기
        self.destroy_monster(spawn_ids=[101,105,111,112,113,114,115,116,117,118,119,120,1001,1011,1021])
        self.spawn_monster(spawn_ids=[105]) # NPC 생성 : 꼬마유령 마리엔
        self.move_user(map_id=63000070, portal_id=11) # 연출포인트로 PC 이동
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene2_marienneappears_set(self.ctx)


class scene2_marienneappears_set(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8020], return_view=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        # 연출용 오브젝트 서류가방 : 반응가능 상태로 만들어 보이게 처리
        self.set_interact_object(trigger_ids=[32000015], state=1)
        self.set_mesh(trigger_ids=[529]) # 연출용 오브젝트 서류가방 더미 :  끔
        self.set_scene_skip(state=sceneskip_2, action='exit') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene2_start(self.ctx)


class scene2_start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8021], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        self.set_effect(trigger_ids=[604], visible=True)
        self.move_npc(spawn_id=105, patrol_name='Patrol_girl')
        self.add_cinematic_talk(npc_id=11004308, msg='$63000070_CS__63000070_MAIN__9$', duration=3000) # 여기까지 와줬구나.\n정말 고마워

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene2_girltalk(self.ctx)


class scene2_girltalk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022], return_view=False)
        self.add_cinematic_talk(npc_id=11004308, msg='$63000070_CS__63000070_MAIN__10$', duration=2000) # 이제
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene2_casezoomin(self.ctx)


class scene2_casezoomin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004308, align=Align.Right, msg='$63000070_CS__63000070_MAIN__11$', duration=3000) # 진실을 확인할 시간
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene2_readytosearch(self.ctx)


class sceneskip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=105, patrol_name='Patrol_girl')
        self.set_effect(trigger_ids=[604])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene2_readytosearch(self.ctx)


class scene2_readytosearch(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return scene2_search_ready(self.ctx)


class scene2_search_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene2_search(self.ctx)


class scene2_search(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[32000015], state=0):
            return scene3_ready(self.ctx)


class scene3_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=sceneskip_3, action='exit') # setsceneskip 3 set
        # setsceneskip 3 set
        # setsceneskip 3 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene3_start(self.ctx)


class scene3_start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8020,8021], return_view=False)
        self.add_cinematic_talk(npc_id=11004308, msg='$63000070_CS__63000070_MAIN__12$', duration=3500) # 유언장이네…\n이제 모든 걸 알 것 같아.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene3_girltalk0(self.ctx)


class scene3_girltalk0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8021], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return scene3_girltalk1(self.ctx)


class scene3_girltalk1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 아빠는 날 지키려고 날 지배인 아저씨의 양녀로 만들고\n모든 걸 지배인 아저씨에게 남겼어
        self.add_cinematic_talk(npc_id=11004308, msg='$63000070_CS__63000070_MAIN__13$', duration=5000)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Talk_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return scene3_girltalk2(self.ctx)


class scene3_girltalk2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 나, 마지막 부탁이 있는데 들어줄 수 있어?\n로비에서 만나자.
        self.add_cinematic_talk(npc_id=11004308, msg='$63000070_CS__63000070_MAIN__14$', duration=4500)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Talk_A', duration=4500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4800):
            return scene3_girlgoout(self.ctx)


class scene3_girlgoout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022], return_view=False)
        self.move_npc(spawn_id=105, patrol_name='Patrol_girl_out')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene3_girldisappears(self.ctx)


class scene3_girldisappears(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105]) # NPC 마리엔 소멸
        self.set_effect(trigger_ids=[605], visible=True)
        # Missing State: State,  setsceneskip 3 close
        self.set_scene_skip()
        # setsceneskip 3 close
        # setsceneskip 3 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene3_readytoend(self.ctx)


class sceneskip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105]) # NPC 마리엔 소멸
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene3_readytoend(self.ctx)


class scene3_readytoend(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_portal(portal_id=20, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[605])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return scene_fin(self.ctx)


class scene_fin(trigger_api.Trigger):
    pass


initial_state = standby
