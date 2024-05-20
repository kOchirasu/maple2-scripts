""" trigger/80000023_bonus/80000023_main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198], visible=True) # 뒷문준비 / 막힌 상태
        # 101-4: 용병 우르자들 / 105:연출용 블랙빈
        self.spawn_monster(spawn_ids=[101,102,103,104,105], auto_target=False)
        self.set_portal(portal_id=1) # 출구포털준비 / 꺼놓은 상태

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 안내(self.ctx)


class 안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=1, text_id=26300739, duration=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 몬스터체크(self.ctx)


class 몬스터체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 텍스트 ON : 시간여행자 블랙빈의 용병, 험상궂은 우르자들을 처치하세요!
        self.show_guide_summary(entity_id=1, text_id=26300739, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104]):
            return 길을열어라(self.ctx)


class 길을열어라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # # 가이드 텍스트 OFF : 시간여행자 블랙빈의 용병, 험상궂은 우르자들을 처치하세요!
        self.hide_guide_summary(entity_id=1)
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Dead_A') # 블랙빈 빠잉
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True) # 출구포털 / 활성화
        self.create_item(spawn_ids=[5001]) # 초록코인

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 문열기00(self.ctx)


class 문열기00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 텍스트 ON : 문이 열렸어요. 출구에 있는 빈빈 코인을 주운 후 이동하세요.
        self.show_guide_summary(entity_id=2, text_id=26300740, duration=10000)
        self.set_mesh(trigger_ids=[198]) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 문열기01(self.ctx)


class 문열기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[180,182,184]) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 문열기02(self.ctx)


class 문열기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[181,183,185]) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 문열기03(self.ctx)


class 문열기03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[186,188,190]) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 문열기04(self.ctx)


class 문열기04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[187,189,191]) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 문열기05(self.ctx)


class 문열기05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[192,194,196]) # 뒷문 / 열기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 문열기06(self.ctx)


class 문열기06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[193,195,197]) # 뒷문 / 열기
        self.destroy_monster(spawn_ids=[105]) # 블랙빈 소멸

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    pass


initial_state = 입장
