""" trigger/02100004_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            # 임시 테스트용 CheckUser10_GuildRaid / DungeonStart
            return CheckUser10_GuildRaid(self.ctx)


class CheckUser10_GuildRaid(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=30, start_delay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=199) >= 10:
            return MaxCount10_Start(self.ctx)
        if self.count_users(box_id=199) < 10:
            return MaxCount10_Wait(self.ctx)
        if not self.is_dungeon_room():
            # 룸던전이 아니면 바로 시작
            return MaxCount10_Start(self.ctx)


class MaxCount10_Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=199) >= 10:
            return MaxCount10_Start(self.ctx)
        if self.time_expired(timer_id='99'):
            return MaxCount10_Start(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return MaxCount10_Wait(self.ctx)
        if not self.is_dungeon_room():
            # 룸던전이 아니면 바로 시작
            return MaxCount10_Start(self.ctx)


class MaxCount10_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='99')

    def on_tick(self) -> trigger_api.Trigger:
        return DungeonStart(self.ctx)


# 설명문 출력
class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100004_BF__MAIN__0$')
        self.set_skip(state=Caption01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Caption01Skip(self.ctx)


class Caption01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001])
        self.close_cinematic()
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[601], visible=True)
        self.show_guide_summary(entity_id=20002411, text_id=20002411)
        self.set_user_value(trigger_id=999993, key='BattleStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 라운드시작1(self.ctx)


class 라운드시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002411)
        self.show_count_ui(text='$02100004_BF__MAIN__1$', count=3)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드1(self.ctx)


class 라운드1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='1,10')
        self.set_timer(timer_id='1', seconds=20, start_delay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작2(self.ctx)
        if self.time_expired(timer_id='1'):
            return 라운드시작2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 라운드시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__2$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드2(self.ctx)


class 라운드2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='2', seconds=20, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='2,10')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작3(self.ctx)
        if self.time_expired(timer_id='2'):
            return 라운드시작3(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='2')


class 라운드시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__3$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드3(self.ctx)


class 라운드3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='3', seconds=20, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='3,10')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작4(self.ctx)
        if self.time_expired(timer_id='3'):
            return 라운드시작4(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='3')


class 라운드시작4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__4$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드4(self.ctx)


class 라운드4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='4', seconds=20, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='4,10')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작5(self.ctx)
        if self.time_expired(timer_id='4'):
            return 라운드시작5(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='4')


class 라운드시작5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__5$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드5(self.ctx)


class 라운드5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='5', seconds=20, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='5,10')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작6(self.ctx)
        if self.time_expired(timer_id='5'):
            return 라운드시작6(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='5')


class 라운드시작6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__6$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드6(self.ctx)


class 라운드6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='6', seconds=20, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='6,10')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작7(self.ctx)
        if self.time_expired(timer_id='6'):
            return 라운드시작7(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='6')


class 라운드시작7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__7$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드7(self.ctx)


class 라운드7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='7', seconds=20, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='7,10')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작8(self.ctx)
        if self.time_expired(timer_id='7'):
            return 라운드시작8(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='7')


class 라운드시작8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__8$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드8(self.ctx)


class 라운드8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='8', seconds=20, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='8,10')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작9(self.ctx)
        if self.time_expired(timer_id='8'):
            return 라운드시작9(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='8')


class 라운드시작9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_user_value(trigger_id=999992, key='RoundStart', value=1)
        self.show_count_ui(text='$02100004_BF__MAIN__9$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드9(self.ctx)


class 라운드9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='9', seconds=20, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='9,10')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=199, spawn_ids=[0]):
            return 라운드시작10(self.ctx)
        if self.time_expired(timer_id='9'):
            return 라운드시작10(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='9')


class 라운드시작10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.spawn_monster(spawn_ids=[2000])
        self.show_count_ui(text='$02100004_BF__MAIN__10$', count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라운드10(self.ctx)


class 라운드10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_timer(timer_id='10', seconds=150, start_delay=1, interval=1)
        self.move_random_user(map_id=2100004, portal_id=99, box_id=101, count=1)
        self.set_event_ui(type=0, arg2='10,10')
        self.set_user_value(trigger_id=999995, key='LastRoundStart', value=1) # 트로피 전용

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000]):
            self.reset_timer(timer_id='10')
            return 성공(self.ctx)
        if self.time_expired(timer_id='10'):
            return 실패(self.ctx)

    def on_exit(self) -> None:
        self.set_event_ui(type=0, arg2='0,0')
        self.set_user_value(trigger_id=999995, key='LastRoundEnd', value=1) # 트로피 전용


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999993, key='BattleEnd', value=1)
        self.destroy_monster(spawn_ids=[-1])
        self.set_achievement(trigger_id=9900, type='trigger', achieve='Find02100004')
        self.set_event_ui(type=7, arg2='$02000251_BF__TRIGGER_01_01__0$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02100004_BF__MAIN__11$', arg3='2000', arg4='0')
        self.set_user_value(trigger_id=999993, key='BattleEnd', value=1)
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
