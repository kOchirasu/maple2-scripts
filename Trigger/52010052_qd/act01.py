""" trigger/52010052_qd/act01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000074], quest_states=[2]):
            # 하늘의 안전 확보, 그러나...  완료 가능
            return NPC리젠03_담당관과트리스탄_02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000050], quest_states=[2]):
            # 전 대원 소집령 퀘스트 완료 가능
            return NPC리젠02_담당관과트리스탄(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000037], quest_states=[2]):
            # 함대 최우선 임무 퀘스트 완료
            return NPC리젠01_5대세력담당관(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000075], quest_states=[3]):
            # 미래의 평화를 위해 퀘스트 완료
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000074], quest_states=[3]):
            # 하늘의 안전 확보, 그러나... 퀘스트 완료
            return NPC리젠03_담당관과트리스탄_02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000063], quest_states=[3]):
            # 그를 만나는 곳, 100m 전 퀘스트 완료
            return NPC리젠01_5대세력담당관(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000058], quest_states=[3]):
            # 달라진 트리스탄 퀘스트 완료
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000057], quest_states=[3]):
            # 준비만이 살길이다 퀘스트 완료
            return NPC리젠01_5대세력담당관(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000050], quest_states=[3]):
            # 전 대원 소집령 퀘스트 완료
            return NPC리젠02_담당관과트리스탄(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000043], quest_states=[3]):
            # 함대 최우선 임무 퀘스트 완료
            return NPC리젠03_트리스탄솔로(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000049], quest_states=[3]):
            # 함대 최우선 임무 퀘스트 완료
            return NPC리젠02_담당관과트리스탄(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000046], quest_states=[3]):
            # 함대 최우선 임무 퀘스트 완료
            return NPC리젠01_5대세력담당관(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000019], quest_states=[3]):
            # 함대 최우선 임무 퀘스트 완료
            return 종료(self.ctx)


class NPC리젠03_트리스탄솔로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2005], auto_target=False) # 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class NPC리젠01_5대세력담당관(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 블리체
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 콘대르
        self.spawn_monster(spawn_ids=[2002], auto_target=False) # 메이슨
        self.spawn_monster(spawn_ids=[2003], auto_target=False) # 샤텐
        self.spawn_monster(spawn_ids=[2004], auto_target=False) # 네이린

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class NPC리젠02_담당관과트리스탄(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 블리체
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 콘대르
        self.spawn_monster(spawn_ids=[2002], auto_target=False) # 메이슨
        self.spawn_monster(spawn_ids=[2003], auto_target=False) # 샤텐
        self.spawn_monster(spawn_ids=[2004], auto_target=False) # 네이린
        self.spawn_monster(spawn_ids=[2005], auto_target=False) # 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000057], quest_states=[3]):
            # 준비만이 살길이다 완료
            return 트리스탄삐짐01(self.ctx)


class 트리스탄삐짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003790, illust_id='Tristan_normal', msg='$52010052_QD__ACT01__0$', duration=4000) # 11003790: 트리스탄
        self.move_npc(spawn_id=2005, patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 트리스탄삐짐02(self.ctx)


class 트리스탄삐짐02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[2005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class NPC리젠03_담당관과트리스탄_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 블리체
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 콘대르
        self.spawn_monster(spawn_ids=[2002], auto_target=False) # 메이슨
        self.spawn_monster(spawn_ids=[2003], auto_target=False) # 샤텐
        self.spawn_monster(spawn_ids=[2004], auto_target=False) # 네이린
        self.spawn_monster(spawn_ids=[2005], auto_target=False) # 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
