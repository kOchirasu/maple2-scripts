""" trigger/02000298_bf/number.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[610])
        self.set_effect(trigger_ids=[611])
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_mesh(trigger_ids=[3224,3225,3226])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[198]):
            return 암호체크(self.ctx)


class 암호체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002982, text_id=20002982)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=197, spawn_ids=[1279]):
            return 입력대기중_1279(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1238]):
            return 입력대기중_1238(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1358]):
            return 입력대기중_1358(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1489]):
            return 입력대기중_1489(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1567]):
            return 입력대기중_1567(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1679]):
            return 입력대기중_1679(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2389]):
            return 입력대기중_2389(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2347]):
            return 입력대기중_2347(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2478]):
            return 입력대기중_2478(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2456]):
            return 입력대기중_2456(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2569]):
            return 입력대기중_2569(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2678]):
            return 입력대기중_2678(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[3458]):
            return 입력대기중_3458(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[3589]):
            return 입력대기중_3589(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[3679]):
            return 입력대기중_3679(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[3789]):
            return 입력대기중_3789(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[4567]):
            return 입력대기중_4567(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[4578]):
            return 입력대기중_4578(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[4689]):
            return 입력대기중_4689(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[4789]):
            return 입력대기중_4789(self.ctx)


class 입력대기중_1279(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000001,12000002,12000007,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000008], state=0):
            return 오답(self.ctx)


class 입력대기중_1238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000001,12000002,12000003,12000008], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_1358(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000001,12000003,12000005,12000008], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_1489(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000001,12000004,12000008,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)


class 입력대기중_1567(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000001,12000005,12000006,12000007], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000008], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_1679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000001,12000006,12000007,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000008], state=0):
            return 오답(self.ctx)


class 입력대기중_2389(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000002,12000003,12000008,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)


class 입력대기중_2347(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000002,12000003,12000004,12000007], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000008], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_2478(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000002,12000004,12000007,12000008], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_2456(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000002,12000004,12000005,12000006], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000008], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_2569(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000002,12000005,12000006,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000008], state=0):
            return 오답(self.ctx)


class 입력대기중_2678(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000002,12000006,12000007,12000008], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_3458(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000003,12000004,12000005,12000008], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_3589(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000003,12000005,12000008,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)


class 입력대기중_3679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000003,12000006,12000007,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000008], state=0):
            return 오답(self.ctx)


class 입력대기중_3789(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000003,12000007,12000008,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000004], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)


class 입력대기중_4567(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000004,12000005,12000006,12000007], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000008], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_4578(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000004,12000005,12000007,12000008], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000009], state=0):
            return 오답(self.ctx)


class 입력대기중_4689(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000004,12000006,12000008,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000007], state=0):
            return 오답(self.ctx)


class 입력대기중_4789(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000004,12000007,12000008,12000009], state=0):
            return 정답(self.ctx)
        if self.object_interacted(interact_ids=[12000001], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000002], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000003], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000005], state=0):
            return 오답(self.ctx)
        if self.object_interacted(interact_ids=[12000006], state=0):
            return 오답(self.ctx)


class 정답(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002982)
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=20002983, text_id=20002983)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20002983)
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_mesh(trigger_ids=[3221,3222,3223], fade=5.0)
        self.set_mesh(trigger_ids=[3224,3225,3226], visible=True, start_delay=1000, interval=1000, fade=5.0)
        self.show_guide_summary(entity_id=20002984, text_id=20002984)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.hide_guide_summary(entity_id=20002984)
            return 종료(self.ctx)


class 오답(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002982)
        self.set_effect(trigger_ids=[610], visible=True)
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=20002985, text_id=20002985)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[12000001,12000002,12000003,12000004,12000005,12000006,12000007,12000008,12000009], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20002985)
            return 방어모드(self.ctx)


class 방어모드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_effect(trigger_ids=[611], visible=True)
        self.show_guide_summary(entity_id=20002986, text_id=20002986)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.spawn_monster(spawn_ids=[1098,1099])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1098,1099]):
            self.hide_guide_summary(entity_id=20002986)
            self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_effect(trigger_ids=[611])
            return 암호체크(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
