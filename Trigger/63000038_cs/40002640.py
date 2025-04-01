""" trigger/63000038_cs/40002640.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_off')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_off')
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107])
        self.set_mesh(trigger_ids=[3400], visible=True)
        self.set_mesh(trigger_ids=[3401], visible=True)
        self.set_sound(trigger_id=13500)
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199], job_code=100):
            return 퀘스트분기_스트라이커(self.ctx)
        if self.user_detected(box_ids=[199], job_code=110):
            return 퀘스트분기_소울바인더(self.ctx)


class 퀘스트분기_스트라이커(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[101], quest_ids=[40002640], quest_states=[1]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(box_ids=[101], quest_ids=[40002640], quest_states=[2]):
            self.move_user(map_id=63000038, portal_id=2)
            return 수락대기40002641(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002640], quest_states=[3]):
            self.move_user(map_id=63000038, portal_id=2)
            return 수락대기40002641(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002641], quest_states=[1]):
            self.move_user(map_id=63000038, portal_id=2)
            return 포털생성(self.ctx)


class 퀘스트분기_소울바인더(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[101], quest_ids=[40002650], quest_states=[1]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(box_ids=[101], quest_ids=[40002650], quest_states=[2]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(box_ids=[101], quest_ids=[40002650], quest_states=[3]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(box_ids=[101], quest_ids=[40002651], quest_states=[1]):
            return 차연출시작1(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002651], quest_states=[2]):
            self.move_user(map_id=63000038, portal_id=2)
            return 완료가능40002651(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002651], quest_states=[3]):
            self.move_user(map_id=63000038, portal_id=2)
            return 완료가능40002651(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002652], quest_states=[1]):
            self.move_user(map_id=63000040, portal_id=1)
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002652], quest_states=[2]):
            self.move_user(map_id=63000040, portal_id=1)
            return 종료(self.ctx)


class 차연출시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=2001, sequence_name='Attack_Idle_A', duration=10000000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199], job_code=100):
            self.spawn_monster(spawn_ids=[1001], auto_target=False)
            self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Attack_Idle_A', duration=10000000000.0)
            return 차연출딜레이1(self.ctx)
        if self.user_detected(box_ids=[199], job_code=110):
            self.spawn_monster(spawn_ids=[11001], auto_target=False)
            self.set_npc_emotion_loop(spawn_id=11001, sequence_name='Attack_Idle_A', duration=10000000000.0)
            return 차연출딜레이1(self.ctx)


class 차연출딜레이1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=차연출종료1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차연출종료1(self.ctx)


class 차연출종료1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)
        self.spawn_monster(spawn_ids=[2101,2102], auto_target=False)
        self.set_user_value(trigger_id=99999002, key='Setlever', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2101]):
            return 계단생성(self.ctx)
        if self.monster_dead(spawn_ids=[2102]):
            return 계단생성(self.ctx)


class 계단생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2001])
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=2002, sequence_name='Attack_Idle_A', duration=10000000000.0)
        self.destroy_monster(spawn_ids=[2101,2102])
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 차전투대기2(self.ctx)


class 차전투대기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199], job_code=100):
            self.destroy_monster(spawn_ids=[1001])
            self.spawn_monster(spawn_ids=[1002], auto_target=False)
            self.set_npc_emotion_loop(spawn_id=1002, sequence_name='Attack_Idle_A', duration=10000000000.0)
            return 차전투2(self.ctx)
        if self.user_detected(box_ids=[199], job_code=110):
            self.destroy_monster(spawn_ids=[11001])
            self.spawn_monster(spawn_ids=[11002], auto_target=False)
            self.set_npc_emotion_loop(spawn_id=11002, sequence_name='Attack_Idle_A', duration=10000000000.0)
            return 차전투2(self.ctx)


class 차전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2103]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3400])
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_on')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103], job_code=100):
            return 차연출시작2(self.ctx)
        if self.user_detected(box_ids=[103], job_code=110):
            return 차연출시작_소울바인더2(self.ctx)


class 차연출시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 칸두라대사01(self.ctx)


class 칸두라대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__0$', time=3)
        self.set_skip(state=칸두라대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 칸두라대사02(self.ctx)


class 칸두라대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸두라대사02(self.ctx)


class 칸두라대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__1$', time=5)
        self.set_skip(state=칸두라대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 칸두라공격(self.ctx)


class 칸두라대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸두라공격(self.ctx)


class 칸두라공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_npc_emotion_sequence(spawn_id=2002, sequence_name='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 칸두라공격이펙트(self.ctx)


class 칸두라공격이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 가로막기(self.ctx)


class 가로막기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 처맞기(self.ctx)


class 처맞기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.select_camera(trigger_id=304)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 처맞기후딜레이(self.ctx)


class 처맞기후딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_npc_emotion_loop(spawn_id=1002, sequence_name='Down_Idle_A', duration=10000000000.0)
            return NPC대사01(self.ctx)


class NPC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=307)
        self.set_dialogue(type=2, spawn_id=11001782, script='$63000038_CS__40002640__2$', time=3)
        self.set_skip(state=NPC대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC대사02(self.ctx)


class NPC대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return NPC대사02(self.ctx)


class NPC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001782, script='$63000038_CS__40002640__3$', time=4)
        self.set_skip(state=NPC대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 칸두라대사03(self.ctx)


class NPC대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸두라대사03(self.ctx)


class 칸두라대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__4$', time=5)
        self.set_skip(state=칸두라대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 칸투라이동(self.ctx)


class 칸두라대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸투라이동(self.ctx)


class 차연출시작_소울바인더2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 칸두라대사01_소울바인더(self.ctx)


class 칸두라대사01_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__5$', time=4)
        self.set_skip(state=칸두라대사01스킵_소울바인더)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 칸두라대사02_소울바인더(self.ctx)


class 칸두라대사01스킵_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸두라대사02_소울바인더(self.ctx)


class 칸두라대사02_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__6$', time=4)
        self.set_skip(state=칸두라대사02스킵_소울바인더)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 칸두라공격_소울바인더(self.ctx)


class 칸두라대사02스킵_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸두라공격_소울바인더(self.ctx)


class 칸두라공격_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_npc_emotion_sequence(spawn_id=2002, sequence_name='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 칸두라공격이펙트_소울바인더(self.ctx)


class 칸두라공격이펙트_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 가로막기_소울바인더(self.ctx)


class 가로막기_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.move_npc(spawn_id=11002, patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 처맞기_소울바인더(self.ctx)


class 처맞기_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.select_camera(trigger_id=304)
        self.move_npc(spawn_id=11002, patrol_name='MS2PatrolData_1002B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 처맞기후딜레이_소울바인더(self.ctx)


class 처맞기후딜레이_소울바인더(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_npc_emotion_loop(spawn_id=11002, sequence_name='Down_Idle_A', duration=10000000000.0)
            return 칸두라대사03_소울바인더(self.ctx)


class 칸두라대사03_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__7$', time=3)
        self.set_skip(state=칸두라대사03스킵_소울바인더)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 칸두라대사04_소울바인더(self.ctx)


class 칸두라대사03스킵_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸두라대사04_소울바인더(self.ctx)


class 칸두라대사04_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__8$', time=6)
        # Missing State: 칸두라대사04스킵_소울바인더
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 칸투라이동(self.ctx)


class 칸두라대사04스킵_소울바인더_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸투라이동(self.ctx)


class 칸투라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2104,2105], auto_target=False)
        # self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차연출종료2(self.ctx)


class 차연출종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=305, enable=False)
        self.destroy_monster(spawn_ids=[2002])
        self.spawn_monster(spawn_ids=[2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FirstPhaseEnd') == 1:
            self.set_mesh(trigger_ids=[3401])
            self.set_actor(trigger_id=202, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_on')
            return 차연출시작3(self.ctx)


class 차연출시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[2104,2105])
        self.select_camera(trigger_id=306)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 차연출분기3(self.ctx)


class 차연출분기3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199], job_code=100):
            return 차연출종료3(self.ctx)
        if self.user_detected(box_ids=[199], job_code=110):
            return NPC교체_소울바인더(self.ctx)


class NPC교체_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='KillallShadow')
        self.destroy_monster(spawn_ids=[11002])
        self.spawn_monster(spawn_ids=[11003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 차연출종료3(self.ctx)


class 차연출종료3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99999004, key='BossGuide', value=1)
        self.select_camera(trigger_id=307, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ChangeBGM') == 1:
            return HP50퍼센트대기(self.ctx)


class HP50퍼센트대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=13500, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CallFriendlyNPC') == 1:
            return 차소환분기4(self.ctx)


class 차소환분기4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199], job_code=100):
            self.destroy_monster(spawn_ids=[1002])
            self.spawn_monster(spawn_ids=[1003])
            return NPC소환(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002651], quest_states=[1]):
            self.destroy_monster(spawn_ids=[11003])
            self.spawn_monster(spawn_ids=[11004])
            return NPC소환(self.ctx)


class NPC소환(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd') == 1:
            return NPC원위치딜레이(self.ctx)


class NPC원위치딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=13500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차원위치분기5(self.ctx)


class 차원위치분기5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199], job_code=100):
            return NPC원위치(self.ctx)
        if self.user_detected(box_ids=[199], job_code=110):
            return NPC원위치_소울바인더(self.ctx)


class NPC원위치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=104, spawn_ids=[1003]):
            return 수락대기40002641(self.ctx)


class 수락대기40002641(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1003])
        self.spawn_monster(spawn_ids=[1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002641], quest_states=[1]):
            return 포털생성(self.ctx)


class NPC원위치_소울바인더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=11004, patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=104, spawn_ids=[11004]):
            return 소울바인더연출시작(self.ctx)


class 소울바인더연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=63000038, portal_id=3)
        self.destroy_monster(spawn_ids=[11004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 준타틴차이등장(self.ctx)


class 준타틴차이등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[13001,13002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 준타대사01(self.ctx)


class 준타대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=308)
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000038_CS__40002640__9$', time=5)
        self.set_skip(state=준타대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 칸두라대사05(self.ctx)


class 준타대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸두라대사05(self.ctx)


class 칸두라대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=311)
        self.spawn_monster(spawn_ids=[2004], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=2004, sequence_name='Attack_Idle_A', duration=10000000000.0)
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__10$', time=5)
        self.set_skip(state=칸두라대사05스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 칸두라대사06(self.ctx)


class 칸두라대사05스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칸두라대사06(self.ctx)


class 칸두라대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000038_CS__40002640__11$', time=3)
        self.set_skip(state=칸두라대사06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 비전등장(self.ctx)


class 칸두라대사06스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 비전등장(self.ctx)


class 비전등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=309)
        self.spawn_monster(spawn_ids=[14001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 칸두라공격02(self.ctx)


class 칸두라공격02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_npc_emotion_sequence(spawn_id=2004, sequence_name='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 비전대신맞기(self.ctx)


class 비전대신맞기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=310)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 비전대신맞기이펙트(self.ctx)


class 비전대신맞기이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera(trigger_id=312)
        self.set_effect(trigger_ids=[603], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 동영상시작(self.ctx)


class 동영상시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Cut_Farewell_Vision.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 완료가능40002651(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=199, type='trigger', achieve='DisappearKandura')


class 완료가능40002651(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=310, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[13001,13002,14001,2004])
        self.spawn_monster(spawn_ids=[13003,13004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002652], quest_states=[1]):
            self.move_user(map_id=63000040, portal_id=1)
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002652], quest_states=[2]):
            self.move_user(map_id=63000040, portal_id=1)
            return 종료(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26300381, text_id=26300381, duration=3000)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
