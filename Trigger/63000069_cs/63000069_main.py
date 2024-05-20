""" trigger/63000069_cs/63000069_main.xml """
import trigger_api


class standby(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        # 연출용 NPC 준비 : 꼬마유령 마리엔 빼고 모두 생성
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106,107,108,109], auto_target=False)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_mesh(trigger_ids=[4001])
        # 연출용 NPC 이동 : 움직임 없는 09번 어린 여자아이 유령 제외 전체 어슬렁어슬렁
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_01_girl')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_02_man')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_03_girlmaid')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_04_boymaid')
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_05_blackstaragent')
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_06_oldman')
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_07_cat')
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_08_youngboy')
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            # <transition state="scene1_ready"/>
            return questcheck(self.ctx)


class questcheck(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[150]) # 연출용 NPC : 꼬마유령 마리엔 지우기
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000356], quest_states=[3]):
            # 완료 이후에는 연출 출력 없음
            return fin(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000356], quest_states=[2]):
            # 완료 가능시 마리엔 등장 연출
            return scene1_ready(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000356], quest_states=[1]):
            # 퀘스트하러 왔을 때는 가이드 스트링
            return searching_check(self.ctx)


class searching_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26300691, text_id=26300691) # 단서 찾으라는 가이드 스트링 출력

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[30000356], quest_states=[2]):
            # 완료 가능 시 연출
            return scene1_ready(self.ctx)


class scene1_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        self.hide_guide_summary(entity_id=26300691, text_id=26300691) # 단서 찾으라는 가이드 스트링 감춤
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # 연출용 NPC 여자 메이드 이동 : 카메라에 걸리지 않는 위치로 멀리 보내기
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_03_girlmaid_out')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return scene1_set(self.ctx)


class scene1_set(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000069, portal_id=11) # 안전포인트로 PC 이동
        self.set_mesh(trigger_ids=[4001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[30000356], quest_states=[2]):
            return questcheck(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return scene1_start(self.ctx)


class scene1_start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        self.set_scene_skip(state=sceneskip, action='exit') # setsceneskip set
        # setsceneskip set
        # setsceneskip set
        self.select_camera_path(path_ids=[8000,8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene1_girlmonologue0(self.ctx)


class scene1_girlmonologue0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[150], auto_target=False) # 연출용 NPC 준비 : 마리엔 생성
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene1_girlmonologue1(self.ctx)


class scene1_girlmonologue1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=150, patrol_name='MS2PatrolData_50_marienne')
        self.set_effect(trigger_ids=[601])
        # 맞지? 내 말.\n아빠 친구, 여기 왔었어.
        self.add_cinematic_talk(npc_id=11004308, msg='$63000069_CS__63000069_MAIN__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene1_girlmonologue2(self.ctx)


class scene1_girlmonologue2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 아빠 친구, 나랑 지배인 아저씨한테 할 말이 있다고 했는데…\n사라져 버렸어.
        self.add_cinematic_talk(npc_id=11004308, msg='$63000069_CS__63000069_MAIN__1$', duration=4500)
        self.set_npc_emotion_loop(spawn_id=150, sequence_name='Talk_A', duration=4500.0)
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene1_girlmonologue3(self.ctx)


class scene1_girlmonologue3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 나한텐 아무도 없었어…\n아빠도… 아빠 친구도…
        self.add_cinematic_talk(npc_id=11004308, msg='$63000069_CS__63000069_MAIN__2$', duration=5500)
        self.set_npc_emotion_loop(spawn_id=150, sequence_name='Bore_B', duration=5500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return scene1_girlrealize0(self.ctx)


class scene1_girlrealize0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_cinematic_talk(npc_id=11004308, msg='$63000069_CS__63000069_MAIN__3$', duration=3000) # ……아
        self.set_npc_emotion_loop(spawn_id=150, sequence_name='Damg_A', duration=100.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene1_girlrealize1(self.ctx)


class scene1_girlrealize1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.add_cinematic_talk(npc_id=11004308, msg='$63000069_CS__63000069_MAIN__4$', duration=4000) # 그런데… 나…
        self.move_user(map_id=63000069, portal_id=10) # 연출포인트로 PC 이동
        self.move_npc(spawn_id=150, patrol_name='MS2PatrolData_51_marienne1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene1_girlrealize2(self.ctx)


class scene1_girlrealize2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 나… 아저씨 방에서 누가 나오는 걸 봤어.\n유언장…이라고 적힌 걸 갖고 444호 객실로 가는 걸 말야.
        self.add_cinematic_talk(npc_id=11004308, msg='$63000069_CS__63000069_MAIN__5$', duration=5000)
        self.set_npc_emotion_loop(spawn_id=150, sequence_name='Talk_A', duration=4500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene1_girlmonologue5(self.ctx)


class scene1_girlmonologue5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.add_cinematic_talk(npc_id=11004308, msg='$63000069_CS__63000069_MAIN__6$', duration=3500) # 이 사실을 알려줘.\n지배인 아저씨께…
        self.set_effect(trigger_ids=[602], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return scene_readytoend(self.ctx)


class scene_readytoend(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불끄기
        self.set_mesh(trigger_ids=[4001])
        # Missing State: State,  setsceneskip close
        self.set_scene_skip()
        # setsceneskip close
        # setsceneskip close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_fin_ready(self.ctx)


class sceneskip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[150]) # NPC 마리엔 소멸
        self.set_mesh(trigger_ids=[4001])
        self.move_user(map_id=63000069, portal_id=10) # 연출포인트로 PC 이동
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_fin_ready(self.ctx)


class scene_fin_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.destroy_monster(spawn_ids=[150]) # NPC 마리엔 소멸
        self.set_effect(trigger_ids=[602])
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_03_girlmaid')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_fin(self.ctx)


class scene_fin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 불켜기
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class fin(trigger_api.Trigger):
    pass


initial_state = standby
