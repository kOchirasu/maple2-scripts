""" trigger/52000092_qd/52000092_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_gravity(gravity=-39.0)
        self.spawn_monster(spawn_ids=[800], auto_target=False) # 오르데 소환
        self.set_mesh(trigger_ids=[900])
        self.set_effect(trigger_ids=[901])
        self.set_effect(trigger_ids=[902])
        self.set_effect(trigger_ids=[903])
        self.set_effect(trigger_ids=[904])
        self.set_effect(trigger_ids=[905])
        self.set_effect(trigger_ids=[906])
        self.set_effect(trigger_ids=[907])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 중력감지메시지(self.ctx)


class 퀘스트체크50100520(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[3]):
            return 이동52000091(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[2]):
            return 이동52000091(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[1]):
            return 이동52000091(self.ctx)


class 중력감지메시지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25200921, text_id=25200921, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100510], quest_states=[1]):
            return 진행중일때20002276(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002276], quest_states=[1]):
            return 진행중일때20002276(self.ctx)


class 진행중일때20002276(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 마법진이 표시된다
        self.set_mesh(trigger_ids=[900], visible=True, fade=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100510], quest_states=[2]):
            return 완료가능할때20002276(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002276], quest_states=[2]):
            return 완료가능할때20002276(self.ctx)


class 완료가능할때20002276(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 마법진이 활성화된다
        self.set_mesh(trigger_ids=[900], fade=100.0)
        self.set_effect(trigger_ids=[901], visible=True)
        self.set_effect(trigger_ids=[902], visible=True)
        self.set_effect(trigger_ids=[903], visible=True)
        self.set_effect(trigger_ids=[904], visible=True)
        self.set_effect(trigger_ids=[905], visible=True)
        self.set_effect(trigger_ids=[906], visible=True)
        self.set_effect(trigger_ids=[907], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[50100520], quest_states=[2]):
            return 완료시01_50100520(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002277], quest_states=[2]):
            return None # Missing State: 완료시01_20002277


# 챕터10 [20002277]완료 시 연출, 오르데가 마법을 발동시킨다.
class 완료시01_50100520(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return None # Missing State: 완료시02_50100520


class 완료시02_20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료시03_20002277(self.ctx)


class 완료시03_20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=800, patrol_name='MS2PatrolData_ordeMove') # 오르데 이동
        self.select_camera_path(path_ids=[2000,2001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료시04_20002277(self.ctx)


class 완료시04_20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2002,2003,2004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료시05_20002277(self.ctx)


class 완료시05_20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2005,2006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료시06_20002277(self.ctx)


class 완료시06_20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2007,2008], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=800, sequence_name='IceSphere_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료시07_20002277(self.ctx)


class 완료시07_20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2009,2010], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료시08_20002277(self.ctx)


class 완료시08_20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 완료20002277(self.ctx)


class 완료20002277(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=52000092)


class 이동52000091(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=52000091)


initial_state = 대기
