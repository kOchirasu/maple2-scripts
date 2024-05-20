""" trigger/52020008_qd/52020008_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[9991])
        self.set_visible_breakable_object(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009])
        self.set_visible_breakable_object(trigger_ids=[6001,6002])
        self.set_visible_breakable_object(trigger_ids=[7001,7002])
        self.set_breakable(trigger_ids=[6001,6002])
        self.set_breakable(trigger_ids=[7001,7002])
        self.set_portal(portal_id=1)
        self.set_agent(trigger_ids=[9001], visible=True)
        self.set_agent(trigger_ids=[9002], visible=True)
        self.set_agent(trigger_ids=[9003], visible=True)
        self.set_agent(trigger_ids=[9004], visible=True)
        self.set_agent(trigger_ids=[9005], visible=True)
        self.set_agent(trigger_ids=[9006], visible=True)
        self.set_agent(trigger_ids=[9007], visible=True)
        self.set_agent(trigger_ids=[9008], visible=True)
        self.set_agent(trigger_ids=[9009], visible=True)
        self.set_agent(trigger_ids=[9010], visible=True)
        self.set_agent(trigger_ids=[9011], visible=True)
        self.set_agent(trigger_ids=[9012], visible=True)
        self.set_agent(trigger_ids=[9013], visible=True)
        self.set_agent(trigger_ids=[9014], visible=True)
        self.set_agent(trigger_ids=[9015], visible=True)
        self.set_agent(trigger_ids=[9016], visible=True)
        self.set_agent(trigger_ids=[9017], visible=True)
        self.set_agent(trigger_ids=[9018], visible=True)
        self.set_agent(trigger_ids=[9019], visible=True)
        self.set_agent(trigger_ids=[9020], visible=True)
        self.set_agent(trigger_ids=[9021], visible=True)
        self.set_agent(trigger_ids=[9022], visible=True)
        self.set_agent(trigger_ids=[9023], visible=True)
        self.set_agent(trigger_ids=[9024], visible=True)
        self.set_agent(trigger_ids=[9025], visible=True)
        self.set_agent(trigger_ids=[9026], visible=True)
        self.set_agent(trigger_ids=[9027], visible=True)
        self.set_agent(trigger_ids=[9028], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 연출카메라1(self.ctx)


class 연출카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=연출종료, action='exit')
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False, delay=30000)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=503)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출카메라1_세리하대사1(self.ctx)


class 연출카메라1_세리하대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003660, script='왕녀는 내가 잘 모실테니 이제 항복하시지?', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출카메라1_크란츠대사1(self.ctx)


class 연출카메라1_크란츠대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=504)
        self.set_dialogue(type=2, spawn_id=11003675, script='아름답지 않은 시중을 받을 생각은 없다!!', time=3)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출카메라1_PC대사1(self.ctx)


class 연출카메라1_PC대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)
        self.set_dialogue(type=1, script='저녀석은 흑성회의 일원이야! 조심해!', time=3)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Troubled_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출카메라1_이오네대사1(self.ctx)


class 연출카메라1_이오네대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=505)
        self.set_dialogue(type=2, spawn_id=11003674, script='시커먼 속내를 가진 건 메이플 연합도 마찬가지 아닌가요? \\n크리티아스의 힘은 누구에게도 이용당하게 두지 않겠어요!', time=5)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출카메라1_세리하대사2(self.ctx)


class 연출카메라1_세리하대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=503)
        self.set_dialogue(type=2, spawn_id=11003660, script='그 말이 맞는 것 같네?\\n세상에 진짜 선과 악은 없는 법이지~', time=3)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출카메라1_흑성회등장(self.ctx)


class 연출카메라1_흑성회등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)
        self.set_dialogue(type=2, spawn_id=11003660, script='이제 어떻게 하실려나?', time=3)
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206,207], auto_target=False)
        self.spawn_monster(spawn_ids=[104,105,106], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출카메라1_탈출장치(self.ctx)


class 연출카메라1_탈출장치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003675, script='이오네님 준비하시죠!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 연출카메라1_벽부수기세팅(self.ctx)


class 연출카메라1_벽부수기세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=507)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출카메라1_레지스탕스등장(self.ctx)


class 연출카메라1_레지스탕스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[9991], enable=True)
        self.set_npc_rotation(spawn_id=103, rotation=270.0)
        self.destroy_monster(spawn_ids=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출카메라1_체키대사1(self.ctx)


class 연출카메라1_체키대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.set_dialogue(type=2, spawn_id=11003661, script='아이고 오늘 정모날인가?', time=3)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출카메라1_세리하대사3(self.ctx)


class 연출카메라1_세리하대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=504)
        self.set_visible_breakable_object(trigger_ids=[6001,6002], visible=True)
        self.set_visible_breakable_object(trigger_ids=[7001,7002], visible=True)
        self.set_breakable(trigger_ids=[6001,6002], enable=True)
        self.set_breakable(trigger_ids=[7001,7002], enable=True)
        self.face_emotion(spawn_id=103, emotion_name='Trigger_bore1')
        self.set_dialogue(type=2, spawn_id=11003660, script='아으... 귀찮아.', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출카메라1_세리하대사4(self.ctx)


class 연출카메라1_세리하대사4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.init_npc_rotation(spawn_ids=[103])
        self.face_emotion(spawn_id=103, emotion_name='Trigger_bore2')
        self.set_dialogue(type=2, spawn_id=11003660, script='왕녀는 또 어디갔어!! 환장하겠네!!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출카메라1_체키대사2(self.ctx)


class 연출카메라1_체키대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.set_visible_breakable_object(trigger_ids=[6001,6002])
        self.set_visible_breakable_object(trigger_ids=[7001,7002])
        self.set_breakable(trigger_ids=[6001,6002])
        self.set_breakable(trigger_ids=[7001,7002])
        self.set_dialogue(type=2, spawn_id=11003661, script='왕녀는 우리가 접수하겠다. 얘들아 처리해라!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출카메라1_체키대사3(self.ctx)


class 연출카메라1_체키대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=104, rotation=180.0)
        self.set_npc_rotation(spawn_id=105, rotation=180.0)
        self.set_npc_rotation(spawn_id=106, rotation=180.0)
        self.set_dialogue(type=2, spawn_id=11003661, script='어서 움직이자!', time=3)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_Chekky')
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_Jigmunt')
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_Henryte')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출카메라1_세리하대사5(self.ctx)


class 연출카메라1_세리하대사5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)
        self.set_dialogue(type=1, spawn_id=103, script='하늘로 솟은거야?? 탑 위에 뭐가 있나 봐야겠어!!', time=3)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_Seriha')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[9991], enable=True)
        self.set_visible_breakable_object(trigger_ids=[6001,6002])
        self.set_visible_breakable_object(trigger_ids=[7001,7002])
        self.set_breakable(trigger_ids=[6001,6002])
        self.set_breakable(trigger_ids=[7001,7002])
        self.destroy_monster(spawn_ids=[-1])
        self.set_visible_breakable_object(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009])
        self.set_breakable(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009])
        self.reset_camera(interpolation_time=0.1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_agent(trigger_ids=[9005])
        self.set_agent(trigger_ids=[9006])
        self.set_agent(trigger_ids=[9007])
        self.set_agent(trigger_ids=[9008])
        self.set_agent(trigger_ids=[9009])
        self.set_agent(trigger_ids=[9010])
        self.set_agent(trigger_ids=[9011])
        self.set_agent(trigger_ids=[9012])
        self.set_agent(trigger_ids=[9013])
        self.set_agent(trigger_ids=[9014])
        self.set_agent(trigger_ids=[9015])
        self.set_agent(trigger_ids=[9016])
        self.set_agent(trigger_ids=[9017])
        self.set_agent(trigger_ids=[9018])
        self.set_agent(trigger_ids=[9019])
        self.set_agent(trigger_ids=[9020])
        self.set_agent(trigger_ids=[9021])
        self.set_agent(trigger_ids=[9022])
        self.set_agent(trigger_ids=[9023])
        self.set_agent(trigger_ids=[9024])
        self.set_agent(trigger_ids=[9025])
        self.set_agent(trigger_ids=[9026])
        self.set_agent(trigger_ids=[9027])
        self.set_agent(trigger_ids=[9028])

    def on_tick(self) -> trigger_api.Trigger:
        return NPC생성(self.ctx)


class NPC생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='세리하를 추적하세요.', arg3='5000')
        self.spawn_monster(spawn_ids=[211,212,213,214,215,216,217])

    def on_tick(self) -> trigger_api.Trigger:
        return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=216, patrol_name='MS2PatrolData_Robot_B')
        self.move_npc(spawn_id=217, patrol_name='MS2PatrolData_Robot_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 계단전투1(self.ctx)


class 계단전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[221])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 계단전투2(self.ctx)


class 계단전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[222])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[211,212,213,214,215,216,217,221,222]):
            return 포탈활성화(self.ctx)


class 포탈활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 감지
