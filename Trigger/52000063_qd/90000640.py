""" trigger/52000063_qd/90000640.xml """
import trigger_api


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100], visible=True)
        self.set_mesh(trigger_ids=[3101])
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004])
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.spawn_monster(spawn_ids=[1001,1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1101,1102,1103,1104,1105], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 퀘스트분기(self.ctx)


class 퀘스트분기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000640], quest_states=[2]):
            return 완료가능90000640(self.ctx)
        if not self.quest_user_detected(box_ids=[199], quest_ids=[90000640], quest_states=[2]):
            return 연출시작(self.ctx)


class 완료가능90000640(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,1002])
        self.spawn_monster(spawn_ids=[1003,1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000640], quest_states=[3]):
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=302)
        self.set_dialogue(type=2, spawn_id=11000168, script='$52000063_QD__90000640__0$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return K대사02(self.ctx)


class K대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1104, patrol_name='MS2PatrolData_1104A')
        self.set_dialogue(type=2, spawn_id=11000168, script='$52000063_QD__90000640__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마칸대사01(self.ctx)


class 마칸대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1101A')
        self.move_npc(spawn_id=1102, patrol_name='MS2PatrolData_1102A')
        self.move_npc(spawn_id=1103, patrol_name='MS2PatrolData_1103A')
        self.move_npc(spawn_id=1105, patrol_name='MS2PatrolData_1105A')
        self.set_dialogue(type=2, spawn_id=11001872, script='$52000063_QD__90000640__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마칸대사02(self.ctx)


class 마칸대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001872, script='$52000063_QD__90000640__3$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=302, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 진행중90000640(self.ctx)


class 진행중90000640(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[101], quest_ids=[90000640], quest_states=[1]):
            self.move_user(map_id=52000063, portal_id=1)
            return 차연출시작2(self.ctx)


class 차연출시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_user_path(patrol_name='MS2PatrolData_PC01')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=303)
        self.set_dialogue(type=2, spawn_id=11000168, script='$52000063_QD__90000640__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return K대사03(self.ctx)


class K대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)
        self.set_dialogue(type=2, spawn_id=11000168, script='$52000063_QD__90000640__5$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100])
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3101], visible=True)
        self.destroy_monster(spawn_ids=[1001,1002])
        self.select_camera(trigger_id=304, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # self.set_event_ui(type=0, arg2='0,0')
        self.show_count_ui(text='$52000063_QD__90000640__6$', stage=1, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 경기시작(self.ctx)


class 경기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99999102, key='gameStart', value=1)
        self.set_user_value(trigger_id=99999103, key='gameStart', value=1)
        self.set_user_value(trigger_id=99999104, key='gameStart', value=1)
        self.create_item(spawn_ids=[9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025])
        self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1101R')
        self.move_npc(spawn_id=1102, patrol_name='MS2PatrolData_1102R')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPC2차이동(self.ctx)


class NPC2차이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1103, patrol_name='MS2PatrolData_1103R')
        self.move_npc(spawn_id=1104, patrol_name='MS2PatrolData_1104R')
        self.move_npc(spawn_id=1105, patrol_name='MS2PatrolData_1105R')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 완료대기(self.ctx)


class 완료대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[9026,9027,9028,9029])
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3101])
        self.spawn_monster(spawn_ids=[1003,1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 완료알림케이대사(self.ctx)


class 완료알림케이대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000168, script='$52000063_QD__90000640__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[9030,9031,9032,9033,9034,9035])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=199, type='trigger', achieve='ArrivedSupercar')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000640], quest_states=[3]):
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기
