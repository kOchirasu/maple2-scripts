""" trigger/02000283_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000427], state=2)
        self.set_interact_object(trigger_ids=[10000430], state=2)
        self.set_interact_object(trigger_ids=[10000431], state=2)
        self.set_interact_object(trigger_ids=[10000432], state=2)
        self.set_interact_object(trigger_ids=[10000433], state=2)
        # mesh.xml 에 있던 내용 2001스폰 아이디의 몬스터가 전투 상태로 되기 전에 죽어버리면 mesh.xml 내용이 작동 안하는 버그가 있어서 mesh.xml  내용을 이 main.xml에 포함시키는 형태로 수정했음
        self.set_portal(portal_id=1)
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355], visible=True)
        self.set_mesh(trigger_ids=[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)
        self.set_interact_object(trigger_ids=[10000427], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000427], state=0):
            return 엘리트스폰(self.ctx)


class 엘리트스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.show_guide_summary(entity_id=20002818, text_id=20002818, duration=5000)
        # mesh.xml 에 있던 내용 2001스폰 아이디의 몬스터가 전투 상태로 되기 전에 죽어버리면 mesh.xml 내용이 작동 안하는 버그가 있어서 mesh.xml  내용을 이 main.xml에 포함시키는 형태로 수정했음
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_random_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355], start_delay=56, fade=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            self.show_guide_summary(entity_id=20002813, text_id=20002813)
            # mesh.xml 에 있던 내용 2001스폰 아이디의 몬스터가 전투 상태로 되기 전에 죽어버리면 mesh.xml 내용이 작동 안하는 버그가 있어서 mesh.xml  내용을 이 main.xml에 포함시키는 형태로 수정했음
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_mesh(trigger_ids=[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416], visible=True, interval=100)
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002813)


initial_state = 대기
