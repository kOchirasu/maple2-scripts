""" trigger/52000187_qd/tutorial.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2000], visible=True) # Invisible
        self.set_portal(portal_id=1)
        self.create_widget(type='Guide')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[90001]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[90002]):
            return 환영(self.ctx)


class 환영(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_quest_accept(quest_id=90000008)
        self.side_npc_talk(npc_id=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[11000071], state=0):
            self.side_npc_talk(npc_id=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__1$')
            self.set_quest_complete(quest_id=90000008)
            return 머쉬킹대화1(self.ctx)


class 머쉬킹대화1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2000]) # Invisible
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[99999], quest_ids=[90000007], quest_states=[1]):
            return 머쉬킹대화2(self.ctx)
        if self.quest_user_detected(box_ids=[99999], quest_ids=[90000007], quest_states=[2]):
            return 머쉬킹대화2(self.ctx)
        if self.quest_user_detected(box_ids=[99999], quest_ids=[90000007], quest_states=[3]):
            return 머쉬킹대화2(self.ctx)


class 머쉬킹대화2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001]) # Invisible

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[90003]):
            self.side_npc_talk(npc_id=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__2$')
            self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_lazy_1')
            return 머쉬킹대화3(self.ctx)


class 머쉬킹대화3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[90004]):
            self.side_npc_talk(npc_id=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__3$')
            return 머쉬킹대화4(self.ctx)


class 머쉬킹대화4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[90005]):
            return 모쿰소환(self.ctx)


class 모쿰소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.add_balloon_talk(spawn_id=102, msg='$52000187_QD__TUTORIAL__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 모쿰이동(self.ctx)


class 모쿰이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_mokum_0')
        self.add_balloon_talk(spawn_id=102, msg='$52000187_QD__TUTORIAL__5$')
        self.side_npc_talk(npc_id=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__6$')
        self.add_buff(box_ids=[99999], skill_id=71000077, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 551:
            # 가이드 To 트리거 -: 몬스터생성신호
            self.spawn_monster(spawn_ids=[101], auto_target=False)
            return 모쿰대사1(self.ctx)


class 모쿰대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_mokum_1')
        self.add_balloon_talk(spawn_id=102, msg='$52000187_QD__TUTORIAL__7$')
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 해제(self.ctx)
        if self.wait_tick(wait_tick=3000):
            return 모쿰대사2(self.ctx)


class 모쿰대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=102, msg='$52000187_QD__TUTORIAL__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 해제(self.ctx)
        if self.wait_tick(wait_tick=3000):
            return 모쿰대사2(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_mokum_2')
        self.guide_event(event_id=560)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[99999], quest_ids=[90000007], quest_states=[3]):
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
