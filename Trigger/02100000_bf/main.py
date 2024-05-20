""" trigger/02100000_bf/main.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[80000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return CheckUser10_GuildRaid(self.ctx)


class CheckUser10_GuildRaid(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30, start_delay=1) # 최대 30초 대기

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=101) >= 10:
            return MaxCount10_Start(self.ctx)
        if self.count_users(box_id=101) < 10:
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=101) >= 10:
            # 10명이면 바로 시작
            return MaxCount10_Start(self.ctx)
        if self.time_expired(timer_id='1'):
            return MaxCount10_Start(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 최대 30초 대기 타이머 초기화
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=904)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100000_BF__MAIN__0$')
        self.set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return ShowCaption01Skip(self.ctx)


class ShowCaption01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return ShowCaption02(self.ctx)


class ShowCaption02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100000_BF__MAIN__1$')
        self.set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CloseCaptionSetting(self.ctx)


class CloseCaptionSetting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.close_cinematic()
        self.select_camera(trigger_id=904, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[101], skill_id=70000133, level=1, is_player=False, is_skill_set=False)
        self.add_buff(box_ids=[101], skill_id=70000133, level=1, is_player=False)
        self.set_effect(trigger_ids=[8001])
        self.set_effect(trigger_ids=[8002])
        self.set_effect(trigger_ids=[8003])
        self.set_mesh(trigger_ids=[80000])
        self.set_skill(trigger_ids=[910001], enable=True)
        self.set_skill(trigger_ids=[910002], enable=True)
        self.set_skill(trigger_ids=[910003], enable=True)
        self.set_skill(trigger_ids=[910004], enable=True)
        self.set_skill(trigger_ids=[910005], enable=True)
        self.set_skill(trigger_ids=[910006], enable=True)
        self.set_skill(trigger_ids=[910007], enable=True)
        self.set_skill(trigger_ids=[910008], enable=True)
        self.set_skill(trigger_ids=[910009], enable=True)
        self.set_skill(trigger_ids=[910010], enable=True)
        self.set_skill(trigger_ids=[910011], enable=True)
        self.set_skill(trigger_ids=[910012], enable=True)
        self.set_skill(trigger_ids=[910013], enable=True)
        self.set_skill(trigger_ids=[910014], enable=True)
        self.set_skill(trigger_ids=[910015], enable=True)
        self.set_skill(trigger_ids=[910016], enable=True)
        self.set_skill(trigger_ids=[910017], enable=True)
        self.set_skill(trigger_ids=[910018], enable=True)
        self.set_skill(trigger_ids=[910019], enable=True)
        self.set_skill(trigger_ids=[910020], enable=True)
        self.set_skill(trigger_ids=[920001], enable=True)
        self.set_skill(trigger_ids=[920002], enable=True)
        self.set_skill(trigger_ids=[920003], enable=True)
        self.set_skill(trigger_ids=[920004], enable=True)
        self.set_skill(trigger_ids=[920005], enable=True)
        self.set_skill(trigger_ids=[920006], enable=True)
        self.set_skill(trigger_ids=[920007], enable=True)
        self.set_skill(trigger_ids=[920008], enable=True)
        self.set_skill(trigger_ids=[920009], enable=True)
        self.set_skill(trigger_ids=[920010], enable=True)
        self.set_skill(trigger_ids=[920011], enable=True)
        self.set_skill(trigger_ids=[920012], enable=True)
        self.set_skill(trigger_ids=[920013], enable=True)
        self.set_skill(trigger_ids=[920014], enable=True)
        self.set_skill(trigger_ids=[920015], enable=True)
        self.set_skill(trigger_ids=[930001], enable=True)
        self.set_skill(trigger_ids=[930002], enable=True)
        self.set_skill(trigger_ids=[930003], enable=True)
        self.set_skill(trigger_ids=[930004], enable=True)
        self.set_skill(trigger_ids=[930005], enable=True)
        self.set_skill(trigger_ids=[930006], enable=True)
        self.set_skill(trigger_ids=[930007], enable=True)
        self.set_skill(trigger_ids=[930008], enable=True)
        self.set_skill(trigger_ids=[930009], enable=True)
        self.set_skill(trigger_ids=[930010], enable=True)
        self.set_skill(trigger_ids=[930011], enable=True)
        self.set_skill(trigger_ids=[930012], enable=True)
        self.set_skill(trigger_ids=[930013], enable=True)
        self.set_skill(trigger_ids=[930014], enable=True)
        self.set_skill(trigger_ids=[930015], enable=True)
        self.set_skill(trigger_ids=[930016], enable=True)
        self.set_skill(trigger_ids=[940001], enable=True)
        self.set_skill(trigger_ids=[940002], enable=True)
        self.set_skill(trigger_ids=[940003], enable=True)
        self.set_skill(trigger_ids=[940004], enable=True)
        self.set_skill(trigger_ids=[940005], enable=True)
        self.set_skill(trigger_ids=[940006], enable=True)
        self.set_skill(trigger_ids=[940007], enable=True)
        self.set_skill(trigger_ids=[940008], enable=True)
        self.set_skill(trigger_ids=[940009], enable=True)
        self.set_skill(trigger_ids=[940010], enable=True)
        self.set_skill(trigger_ids=[940011], enable=True)
        self.set_skill(trigger_ids=[940012], enable=True)
        self.set_skill(trigger_ids=[940013], enable=True)
        self.set_skill(trigger_ids=[940014], enable=True)
        self.set_skill(trigger_ids=[940015], enable=True)
        self.set_skill(trigger_ids=[940016], enable=True)
        self.set_skill(trigger_ids=[940017], enable=True)
        self.set_skill(trigger_ids=[940018], enable=True)
        self.set_skill(trigger_ids=[940019], enable=True)
        self.set_skill(trigger_ids=[940020], enable=True)
        self.set_skill(trigger_ids=[940021], enable=True)
        self.set_skill(trigger_ids=[940022], enable=True)
        self.set_skill(trigger_ids=[940023], enable=True)
        self.set_skill(trigger_ids=[940024], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 버프_2(self.ctx)


class 버프_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02100000_BF__MAIN__2$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 바리케이트(self.ctx)


class 바리케이트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02100000_BF__MAIN__3$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 닫기(self.ctx)


class 닫기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[80000], visible=True)
        self.set_effect(trigger_ids=[8001], visible=True)
        self.set_effect(trigger_ids=[8002], visible=True)
        self.set_effect(trigger_ids=[8003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = Wait
