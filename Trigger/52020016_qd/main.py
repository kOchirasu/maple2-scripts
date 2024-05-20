""" trigger/52020016_qd/main.xml """
import trigger_api
from System.Numerics import Vector3


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=95)
        self.set_portal(portal_id=96)
        self.set_effect(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024])
        self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005])
        # self.set_effect(trigger_ids=[71001,71002,71003,71004,71005,71006,71007,71008,71009,71010,71011,71012,71013,71014,71015,71016])
        self.set_effect(trigger_ids=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012])
        self.set_effect(trigger_ids=[73001,73002,73003,73004,73005,73006,73007,73008,73009,73010,73011,73012])
        self.set_mesh(trigger_ids=[5103,5104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 시작_2(self.ctx)


class 시작_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.select_camera_path(path_ids=[2000004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작_2_2(self.ctx)


class 시작_2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, script='이곳은 뭐하는 곳이지?!', time=3)
        self.set_dialogue(type=2, script='미카엘의 기운이 느껴지고 있어!\\n서둘러야 해!!', time=3)
        self.set_skip(state=시작_3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 시작_3(self.ctx)


class 시작_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 시작_4(self.ctx)


class 시작_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.set_dialogue(type=1, script='한번 가볼까?', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 인트로(self.ctx)


class 인트로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(0,0,0))
        self.set_directional_light(diffuse_color=Vector3(0,0,0))
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.set_pc_emotion_loop(sequence_name='Stun_A', duration=1500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return 인트로_2(self.ctx)


class 인트로_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, script='???!!!', time=2)
        self.set_dialogue(type=2, script='뭐야!!\\n앞이 안보여!!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 인트로_3(self.ctx)


class 인트로_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 미카엘등장(self.ctx)


class 미카엘등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000001], return_view=False)
        self.spawn_monster(spawn_ids=[300001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 미카엘_이동_1(self.ctx)


class 미카엘_이동_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=300001, patrol_name='MS2PatrolData0_300001_0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대화_1(self.ctx)


class 대화_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=300001, script='오호...여기까지 오다니...놀랍군요..', time=5)
        self.set_dialogue(type=2, spawn_id=300001, script='자...그럼 본격적으로 놀아볼까요?', time=5)
        self.set_skip(state=카메라리셋_1)
        self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 카메라리셋_1(self.ctx)


class 카메라리셋_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000001])
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.destroy_monster(spawn_ids=[300001])
        # self.add_buff(box_ids=[102], skill_id=70000102, level=1)
        self.set_effect(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이동_1(self.ctx)


class 이동_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020016, portal_id=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 전투페이즈_1(self.ctx)

    def on_exit(self) -> None:
        self.set_ambient_light(primary=Vector3(180,180,149))
        self.set_directional_light(diffuse_color=Vector3(219,204,182), specular_color=Vector3(219,204,182))
        self.set_portal(portal_id=95, visible=True, enable=True)
        self.set_dialogue(type=1, script='갇혀 버렸어!', time=3)


class 전투페이즈_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 전투종료(self.ctx)

    def on_exit(self) -> None:
        self.set_event_ui(type=1, arg2='미카엘이 조종하는 마리오네트 무리들을 처치하세요.', arg3='4000')
        self.shadow_expedition_open_boss_gauge(max_gauge_point=300, title='몬스터 처치 달성')
        self.set_user_value(trigger_id=901, key='respawn_phase_1', value=1)
        self.set_user_value(trigger_id=902, key='respawn_phase_1', value=1)
        self.set_user_value(trigger_id=903, key='respawn_phase_1', value=1)
        self.set_user_value(trigger_id=904, key='respawn_phase_1', value=1)


class 전투종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 300:
            return 페이즈_2_준비(self.ctx)


class 페이즈_2_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition_close_boss_gauge()
        self.set_user_value(trigger_id=901, key='respawn_phase_1_end', value=1)
        self.set_user_value(trigger_id=902, key='respawn_phase_1_end', value=1)
        self.set_user_value(trigger_id=903, key='respawn_phase_1_end', value=1)
        self.set_user_value(trigger_id=904, key='respawn_phase_1_end', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 불꺼짐(self.ctx)


class 불꺼짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=95)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.set_ambient_light(primary=Vector3(0,0,0))
        self.set_directional_light(diffuse_color=Vector3(0,0,0))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 미카엘등장_2(self.ctx)


class 미카엘등장_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000002], return_view=False)
        self.spawn_monster(spawn_ids=[300002], auto_target=False)
        self.move_npc(spawn_id=300002, patrol_name='MS2PatrolData0_300002_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대화_2(self.ctx)


class 대화_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=300002, script='음... 기대 이상인데요?', time=5)
        self.set_dialogue(type=2, spawn_id=300002, script='이번엔 이분들이 당신과 놀아줄겁니다!!', time=5)
        self.move_user(map_id=52020016, portal_id=91)
        self.set_skip(state=카메라리셋_2)
        self.set_mesh(trigger_ids=[5103,5104], visible=True)
        # self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return npc등장연출_1(self.ctx)


class npc등장연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[310001], auto_target=False)
        # self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return npc등장연출_2(self.ctx)


class npc등장연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[310002], auto_target=False)
        # self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return npc등장연출_3(self.ctx)


class npc등장연출_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[310003], auto_target=False)
        # self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return npc등장연출_4(self.ctx)


class npc등장연출_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[310004], auto_target=False)
        # self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라리셋_2(self.ctx)


class 카메라리셋_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000002])
        # self.set_directional_light(diffuse_color=Vector3(193,180,137), specular_color=Vector3(100,100,100))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1600):
            return 자기장생성(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)


class 자기장생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[300002])
        self.destroy_monster(spawn_ids=[310001])
        self.destroy_monster(spawn_ids=[310002])
        self.destroy_monster(spawn_ids=[310003])
        self.destroy_monster(spawn_ids=[310004])
        # self.add_buff(box_ids=[102], skill_id=70000102, level=1)
        # self.set_effect(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)
        self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005])
        self.set_effect(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024])
        # self.set_effect(trigger_ids=[71001,71002,71003,71004,71005,71006,71007,71008,71009,71010,71011,71012,71013,71014,71015,71016], visible=True)
        self.set_effect(trigger_ids=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012], visible=True)
        self.set_effect(trigger_ids=[73001,73002,73003,73004,73005,73006,73007,73008,73009,73010,73011,73012], visible=True)
        self.set_ambient_light(primary=Vector3(180,180,149))
        self.set_directional_light(diffuse_color=Vector3(219,204,182), specular_color=Vector3(219,204,182))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대화_놀람(self.ctx)


class 대화_놀람(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='아앗! 오스칼과 레드아이, 알론... 그리고 레논?', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 몬스터등장_2(self.ctx)


class 몬스터등장_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=96, visible=True, enable=True)
        self.set_user_value(trigger_id=905, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터등장_2_2(self.ctx)


class 몬스터등장_2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=906, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터등장_2_3(self.ctx)


class 몬스터등장_2_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=907, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터등장_2_4(self.ctx)


class 몬스터등장_2_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=908, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 몬스터사망_1(self.ctx)


class 몬스터사망_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4000101]) and self.monster_dead(spawn_ids=[4000102]) and self.monster_dead(spawn_ids=[4000103]) and self.monster_dead(spawn_ids=[4000104]):
            return 시간종료_3(self.ctx)


"""
class 몬스터등장_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=96, visible=True, enable=True)
        self.set_user_value(trigger_id=905, key='respawn_phase_2', value=1)
        self.set_user_value(trigger_id=906, key='respawn_phase_2', value=1)
        self.set_user_value(trigger_id=907, key='respawn_phase_2', value=1)
        self.set_user_value(trigger_id=908, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 타이머시작(self.ctx)
"""

"""
class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='아앗! 오스칼과 레드아이, 알론... 그리고 레논?', time=3)
        self.set_timer(timer_id='100', seconds=40, start_delay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return 대화(self.ctx)
"""

"""
class 대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='헉헉...그만둬! 모두들!!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 시간종료(self.ctx)
"""

"""
class 시간종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='100'):
            return 시간종료_2(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=905, key='respawn_phase_2_end', value=1)
        self.set_user_value(trigger_id=906, key='respawn_phase_2_end', value=1)
        self.set_user_value(trigger_id=907, key='respawn_phase_2_end', value=1)
        self.set_user_value(trigger_id=908, key='respawn_phase_2_end', value=1)
"""

"""
class 시간종료_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 시간종료_3(self.ctx)
"""

class 시간종료_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(0,0,0))
        self.set_directional_light(diffuse_color=Vector3(193,180,137), specular_color=Vector3(100,100,100))
        self.set_dialogue(type=1, script='모두들...어디로 사라진거야?', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 불꺼짐_2(self.ctx)


class 불꺼짐_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000003], return_view=False)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        # self.set_cinematic_ui(type=3)
        # self.set_cinematic_ui(type=1)
        # self.set_ambient_light(primary=Vector3(0,0,0))
        # self.set_directional_light(diffuse_color=Vector3(0,0,0))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 몬스터등장_3(self.ctx)

    def on_exit(self) -> None:
        self.set_dialogue(type=2, spawn_id=4000201, script='자...기대하세요!', time=5)
        self.set_skip(state=몬스터등장_3)


class 몬스터등장_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012])
        self.set_mesh(trigger_ids=[5104])
        self.set_dialogue(type=1, script='여기서 쓰러질 순 없어!', time=3)
        self.set_user_value(trigger_id=909, key='respawn_phase_3', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 카메라리셋_3(self.ctx)


class 카메라리셋_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000003])
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이동_3(self.ctx)


class 이동_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 이동_4(self.ctx)

    def on_exit(self) -> None:
        self.set_ambient_light(primary=Vector3(180,180,149))
        self.set_directional_light(diffuse_color=Vector3(219,204,182), specular_color=Vector3(219,204,182))


class 이동_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)
        self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005], visible=True)
        self.set_dialogue(type=1, script='아니! 이 녀석들은??!!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = 시작
