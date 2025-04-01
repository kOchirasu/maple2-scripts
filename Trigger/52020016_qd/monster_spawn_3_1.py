""" trigger/52020016_qd/monster_spawn_3_1.xml """
import trigger_api
from System.Numerics import Vector3


class 체력조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn_phase_3') == 1:
            return 전투페이즈(self.ctx)


class 전투페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[4000201], auto_target=False)
        self.spawn_monster(spawn_ids=[4000202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4000201]) and self.monster_dead(spawn_ids=[4000202]):
            return 전투페이즈_2(self.ctx)


class 전투페이즈_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[4000301], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 전투페이즈_2_대사(self.ctx)


class 전투페이즈_2_대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=4000301, script='하하하!!내가 돌아왔다!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='카...카트반? 어떻게?!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4000301]):
            return 대화(self.ctx)

    def on_exit(self) -> None:
        self.set_ambient_light(primary=Vector3(0,0,0))
        self.set_directional_light(diffuse_color=Vector3(0,0,0))


class 대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.set_dialogue(type=2, spawn_id=4000201, script='제법이군요! 그렇다면 이건 어떤가요?', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 조디등장_1(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[4000401], auto_target=False)


class 조디등장_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4000401, patrol_name='MS2PatrolData0_4000401_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 조디등장_2(self.ctx)

    def on_exit(self) -> None:
        self.select_camera_path(path_ids=[2000001], return_view=False)


class 조디등장_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, script='!!!!!!!??????', time=3)
        self.set_dialogue(type=2, script='조...조디?!', time=3)
        self.set_dialogue(type=2, script='조디...살아있었던거야?', time=3)
        self.set_dialogue(type=2, spawn_id=300001, script='헤헤...오랫만에 뵙네요. 보고싶었어요.', time=5)
        self.set_dialogue(type=2, spawn_id=300001, script='그런데 저를...왜 죽게 내버려 두었나요?', time=5)
        self.set_dialogue(type=2, script='그...그게 아니야!!', time=3)
        self.set_dialogue(type=2, spawn_id=300001, script='당신을...저주해요..가만두지 않겠어요!!', time=5)
        self.set_dialogue(type=2, script='아...안돼 그만둬!! 조디!!', time=3)
        self.set_skip(state=마지막전투)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=32000):
            return 마지막전투(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[4000401], arg2=False)
        self.select_camera_path(path_ids=[2000001])


class 마지막전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.destroy_monster(spawn_ids=[4000401])
        self.set_effect(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마지막전투_2(self.ctx)


class 마지막전투_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(180,180,149))
        self.set_directional_light(diffuse_color=Vector3(219,204,182), specular_color=Vector3(219,204,182))
        self.set_portal(portal_id=95, visible=True, enable=True)
        self.set_user_value(trigger_id=911, key='respawn_phase_4', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4000402]):
            return 마지막전투_3(self.ctx)


class 마지막전투_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=912, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=913, key='respawn_phase_4', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4000403]) and self.monster_dead(spawn_ids=[4000404]):
            return 마지막전투_4(self.ctx)


class 마지막전투_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=914, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=915, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=916, key='respawn_phase_4', value=1)
        self.set_dialogue(type=1, script='조디!! 제발 맘춰!!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4000405]) and self.monster_dead(spawn_ids=[4000406]) and self.monster_dead(spawn_ids=[4000407]):
            return 마지막전투_5(self.ctx)


class 마지막전투_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=917, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=918, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=919, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=920, key='respawn_phase_4', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4000408]) and self.monster_dead(spawn_ids=[4000409]) and self.monster_dead(spawn_ids=[4000410]) and self.monster_dead(spawn_ids=[4000411]):
            return 긴급대화_2(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(type='trigger', achieve='DollMaster')


"""
class 마지막전투_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=95, visible=True, enable=True)
        self.set_user_value(trigger_id=911, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=912, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=913, key='respawn_phase_4', value=1)
        self.set_user_value(trigger_id=914, key='respawn_phase_4', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4400):
            return 타이머시작(self.ctx)
"""

"""
class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='115', seconds=30, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 긴급대화(self.ctx)
"""

"""
class 긴급대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='조디!! 제발 맘춰!!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 시간종료(self.ctx)
"""

"""
class 시간종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(type='trigger', achieve='DollMaster')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='115'):
            return 긴급대화_2(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=911, key='respawn_phase_4_end', value=1)
        self.set_user_value(trigger_id=912, key='respawn_phase_4_end', value=1)
        self.set_user_value(trigger_id=913, key='respawn_phase_4_end', value=1)
        self.set_user_value(trigger_id=914, key='respawn_phase_4_end', value=1)
"""

class 긴급대화_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Disappoint_A','Emotion_Disappoint_Idle_A'])
        self.set_dialogue(type=1, script='이젠...더이상은...힘들어....', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 긴급대화_3(self.ctx)


class 긴급대화_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마지막_연출(self.ctx)


class 마지막_연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[400001], auto_target=False)
        self.spawn_monster(spawn_ids=[400002], auto_target=False)
        self.spawn_monster(spawn_ids=[400003], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=400001, sequence_name='Attack_Idle_A', duration=100000000.0)
        self.set_npc_emotion_loop(spawn_id=400002, sequence_name='Attack_Idle_A', duration=100000000.0)
        self.set_npc_emotion_loop(spawn_id=400003, sequence_name='Attack_Idle_A', duration=100000000.0)
        self.move_user(map_id=52020016, portal_id=97)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마지막_연출_2(self.ctx)

    def on_exit(self) -> None:
        self.set_pc_emotion_loop(sequence_name='Emotion_Disappoint_Idle_A', duration=100000000.0)


class 마지막_연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(path_ids=[2000005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마지막_연출_3(self.ctx)


class 마지막_연출_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[320001], auto_target=False)
        self.move_npc(spawn_id=320001, patrol_name='MS2PatrolData0_320001_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마지막_연출_4(self.ctx)


class 마지막_연출_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=320001, script='하하하하! 느껴지시나요? 나와 당신의 높이가!!', time=5)
        self.set_dialogue(type=2, script='헉헉...제발 그만둬!!', time=3)
        self.set_dialogue(type=2, spawn_id=320001, script='이 몽환의 무대 안에서는 어떠한 존재라도 저를 이길 수 없습니다!', time=5)
        self.set_dialogue(type=2, spawn_id=320001, script='그럼 이제 마무리를 지어 볼까요?', time=5)
        self.set_skip(state=마지막_연출_4_2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=17000):
            return 마지막_연출_4_2(self.ctx)


class 마지막_연출_4_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000006], return_view=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 마지막_연출_4_3(self.ctx)


class 마지막_연출_4_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[410001], auto_target=False)
        self.spawn_monster(spawn_ids=[410002], auto_target=False)
        self.spawn_monster(spawn_ids=[410003], auto_target=False)
        self.spawn_monster(spawn_ids=[410004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 마지막_연출_5(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[420001], auto_target=False)
        self.spawn_monster(spawn_ids=[420002], auto_target=False)
        self.spawn_monster(spawn_ids=[420003], auto_target=False)
        self.spawn_monster(spawn_ids=[420004], auto_target=False)
        self.spawn_monster(spawn_ids=[420005], auto_target=False)
        self.spawn_monster(spawn_ids=[420006], auto_target=False)
        self.spawn_monster(spawn_ids=[420007], auto_target=False)


class 마지막_연출_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return 유저이동(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020032, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            pass


initial_state = 체력조건
