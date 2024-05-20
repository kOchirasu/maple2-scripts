""" trigger/99999949/06_questcondition.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[11000064], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9051]):
            self.add_effect_nif(spawn_id=11000064, nif_path='Map\\Royalcity\\Indoor\\ry_in_cubric_mat_A01.nif', is_outline=True, scale=0.5, rotate_z=45)
            self.face_emotion(emotion_name='Ride_Idle_000')
            return Wait2(self.ctx)


class Wait2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='AddEffectNif 테스트')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Guide(self.ctx)

    def on_exit(self) -> None:
        self.remove_effect_nif(spawn_id=11000064)
        self.face_emotion()


class Guide(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='40002673퀘스트 완료가능 or 완료 상태를 만들고 6번 영역안에 들어가보세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9050], quest_ids=[40002673,40002674,40002675,40002676,40002677,40002678,40002679], quest_states=[1]):
            return NpcChange01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[11000064])
        self.spawn_monster(spawn_ids=[11000044], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[11000044])
        self.debug_string(value='5초 후에 트리거가 리셋됩니다. 6번 영역 밖으로 나가세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Wait(self.ctx)


initial_state = Wait
