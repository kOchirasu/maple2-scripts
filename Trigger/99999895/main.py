""" trigger/99999895/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 몬스터스폰대기1(self.ctx)


class 몬스터스폰대기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='첫 번째 상대가 곧 출현합니다. 전투 준비를 하세요!!', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카운트1_1(self.ctx)


class 카운트1_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카운트1_2(self.ctx)


class 카운트1_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카운트1_3(self.ctx)


class 카운트1_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터스폰1(self.ctx)


class 몬스터스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='시작!!', arg3='1000')
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 스폰대사1(self.ctx)


class 스폰대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='네 마음가짐과 기량을 한 번 볼까?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            self.add_balloon_talk(spawn_id=101, msg='너 따위 애송이에게 지다니...', duration=3000)
            return 몬스터스폰대기2(self.ctx)


class 몬스터스폰대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='첫 전투에서 승리하셨습니다. 잠시만 기다려주세요 다음전투가 기다리고 있습니다!!', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카운트2_1(self.ctx)


class 카운트2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카운트2_2(self.ctx)


class 카운트2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카운트2_3(self.ctx)


class 카운트2_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터스폰2(self.ctx)


class 몬스터스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='시작!!', arg3='1000')
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 스폰대사2(self.ctx)


class 스폰대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=102, msg='와라!! 얼마나 성장했는지 보겠다!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            self.add_balloon_talk(spawn_id=102, msg='꽤 하는군. 즐거운 싸움이었다.', duration=3000)
            return 몬스터스폰대기3(self.ctx)


class 몬스터스폰대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='두 번째 전투에서 승리하셨습니다. 잠시만 기다려주세요 마지막 전투가 기다리고 있습니다!!', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카운트3_1(self.ctx)


class 카운트3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카운트3_2(self.ctx)


class 카운트3_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카운트3_3(self.ctx)


class 카운트3_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터스폰3(self.ctx)


class 몬스터스폰3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='시작!!', arg3='1000')
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 스폰대사3(self.ctx)


class 스폰대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=103, msg='그동안 어떤 성과를 이루셨는지 보여주세요.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            self.add_balloon_talk(spawn_id=103, msg='좋은 실력입니다. 엘리넬 학생들에게 귀감이 될 분이시군요.', duration=3000)
            return 대사(self.ctx)


class 대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=7, arg2='SUCCESS', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 안내(self.ctx)


class 안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='곧 다시 전투가 시작됩니다. 준비하세요!!', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대기(self.ctx)


initial_state = 대기
