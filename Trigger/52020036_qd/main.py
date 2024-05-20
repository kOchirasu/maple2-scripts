""" trigger/52020036_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000043], state=2)
        self.set_mesh(trigger_ids=[9999], visible=True) # 발록 함선 보이기
        self.spawn_monster(spawn_ids=[7000])
        self.spawn_monster(spawn_ids=[7001])
        self.spawn_monster(spawn_ids=[7002])
        self.spawn_monster(spawn_ids=[7003])
        self.spawn_monster(spawn_ids=[7004])
        # self.set_mesh(trigger_ids=[4000]) # 공습용 공중 발판 끄기1
        # self.set_mesh(trigger_ids=[4001]) # 공습용 공중 발판 끄기1
        self.set_mesh(trigger_ids=[4002]) # 공습용 공중 발판 끄기1
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 구르는 천둥
        self.spawn_monster(spawn_ids=[901], auto_target=False) # 시끄러운 주먹
        self.spawn_monster(spawn_ids=[400], auto_target=False) # 티나
        self.spawn_monster(spawn_ids=[10000], auto_target=False)
        self.spawn_monster(spawn_ids=[10001], auto_target=False)
        self.spawn_monster(spawn_ids=[10002], auto_target=False)
        self.spawn_monster(spawn_ids=[10003], auto_target=False)
        self.spawn_monster(spawn_ids=[10004], auto_target=False)
        self.spawn_monster(spawn_ids=[10006], auto_target=False)
        self.spawn_monster(spawn_ids=[10007], auto_target=False)
        self.spawn_monster(spawn_ids=[10008], auto_target=False)
        self.spawn_monster(spawn_ids=[10009], auto_target=False)
        self.spawn_monster(spawn_ids=[10010], auto_target=False)
        self.spawn_monster(spawn_ids=[10011], auto_target=False)
        self.spawn_monster(spawn_ids=[10014], auto_target=False)
        self.spawn_monster(spawn_ids=[10015], auto_target=False)
        self.spawn_monster(spawn_ids=[10016], auto_target=False)
        self.spawn_monster(spawn_ids=[10017], auto_target=False)
        self.spawn_monster(spawn_ids=[10018], auto_target=False)
        self.spawn_monster(spawn_ids=[10019], auto_target=False)
        self.spawn_monster(spawn_ids=[10020], auto_target=False)
        self.spawn_monster(spawn_ids=[10021], auto_target=False)
        self.spawn_monster(spawn_ids=[10022], auto_target=False)
        self.spawn_monster(spawn_ids=[10023], auto_target=False)
        self.spawn_monster(spawn_ids=[10024], auto_target=False)
        self.spawn_monster(spawn_ids=[10025], auto_target=False)
        self.spawn_monster(spawn_ids=[10026], auto_target=False)
        self.spawn_monster(spawn_ids=[10027], auto_target=False)
        self.spawn_monster(spawn_ids=[10028], auto_target=False)
        self.spawn_monster(spawn_ids=[10029], auto_target=False)
        self.spawn_monster(spawn_ids=[10030], auto_target=False)
        self.spawn_monster(spawn_ids=[10031], auto_target=False)
        self.spawn_monster(spawn_ids=[10032], auto_target=False)
        self.spawn_monster(spawn_ids=[10033], auto_target=False)
        self.spawn_monster(spawn_ids=[10034], auto_target=False)
        self.spawn_monster(spawn_ids=[10035], auto_target=False)
        self.spawn_monster(spawn_ids=[10036], auto_target=False)
        self.spawn_monster(spawn_ids=[10037], auto_target=False)
        self.spawn_monster(spawn_ids=[10038], auto_target=False)
        self.spawn_monster(spawn_ids=[10039], auto_target=False)
        self.spawn_monster(spawn_ids=[10040], auto_target=False)
        self.spawn_monster(spawn_ids=[10041], auto_target=False)
        self.spawn_monster(spawn_ids=[10042], auto_target=False)
        self.spawn_monster(spawn_ids=[10043], auto_target=False)
        self.spawn_monster(spawn_ids=[10044], auto_target=False)
        self.spawn_monster(spawn_ids=[10045], auto_target=False)
        self.spawn_monster(spawn_ids=[10046], auto_target=False)
        self.spawn_monster(spawn_ids=[10047], auto_target=False)
        self.spawn_monster(spawn_ids=[10048], auto_target=False)
        self.spawn_monster(spawn_ids=[10049], auto_target=False)
        self.spawn_monster(spawn_ids=[10050], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000049], quest_states=[3]):
            # 91000049 퀘스트 완료처리 상태면
            return 공중지원퀘스트완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000049], quest_states=[2]):
            # 91000049 퀘스트 완료처리 상태면
            return 공중지원퀘스트완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000049], quest_states=[1]):
            # 91000049 퀘스트 수락 상태면
            return 네이린팝업1(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000048], quest_states=[3]):
            # 91000048 퀘스트 완료처리 상태면
            return 부상자옮기기대사(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000048], quest_states=[2]):
            # 91000048 퀘스트 완료처리 상태면
            return 부상자옮기기대사(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000048], quest_states=[1]):
            # 91000048 퀘스트 수락 상태면
            return 티나비추기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000047], quest_states=[3]):
            # 91000047 퀘스트 완료처리 상태면
            return 침략자소탕퀘스트완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000047], quest_states=[2]):
            # 91000047 퀘스트 완료처리 상태면
            return 침략자소탕퀘스트완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000047], quest_states=[1]):
            # 91000047 퀘스트 수락 상태면
            return 오프닝연출끝(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 피그밍그부족의제단원경신1(self.ctx)


# 피그밍그 부족의 제단 원경신1
class 피그밍그부족의제단원경신1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_quest_accept(quest_id=91000047)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.show_caption(type='VerticalCaption', title='$52020036_QD__MAIN__0$', desc='$52020036_QD__MAIN__1$', align=Align.Bottom | Align.Left, duration=7000, scale=2.5)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[3000,3001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 피그밍그부족의제단원경신2(self.ctx)


# 피그밍그 부족의 제단 원경신2
class 피그밍그부족의제단원경신2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3013,3014], return_view=False)
        self.set_scene_skip(state=콘대르소환, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 전투상황비추기(self.ctx)


class 전투상황비추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.select_camera(trigger_id=3003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 유저발록보이게위치옮김(self.ctx)


class 유저발록보이게위치옮김(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020036, portal_id=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오프닝크림슨발록비추기(self.ctx)


class 오프닝크림슨발록비추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3015)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨발록오프닝대사(self.ctx)


class 크림슨발록오프닝대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003781, msg='$52020036_QD__MAIN__2$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 콘대르등장카메라(self.ctx)


# 콘대르 등장
class 콘대르등장카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3002)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 콘대르소환(self.ctx)


class 콘대르소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020036, portal_id=1)
        self.spawn_monster(spawn_ids=[100], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 유저를경로이동시킨다(self.ctx)


class 유저를경로이동시킨다(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='User_PatrolData_0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 콘대르등장대사(self.ctx)


class 콘대르등장대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003776, illust_id='Conder_normal', msg='$52020036_QD__MAIN__3$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 콘대르이동(self.ctx)


class 콘대르이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='Conder_Spawn_Opening_PatrolData_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 오프닝연출끝(self.ctx)


class 오프닝연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawn_ids=[100])
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 콘대르
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구르는천둥대사(self.ctx)


# 구르는천둥대사1
class 구르는천둥대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11000009, illust='RollingThunder_normal', duration=7000, script='$52020036_QD__main__12$', voice='ko/Npc/00002150')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 콘대르전투참여대사(self.ctx)


# 콘대르전투참여대사
class 콘대르전투참여대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003776, illust='Conder_normal', duration=8300, script='$52020036_QD__main__13$', voice='ko/Npc/00002147')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8300):
            return 침략자소탕퀘스트완료체크(self.ctx)


class 침략자소탕퀘스트완료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000047], quest_states=[2]):
            return 침략자소탕퀘스트완료(self.ctx)


class 침략자소탕퀘스트완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_quest_complete(quest_id=91000047)
        self.set_quest_accept(quest_id=91000048)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[3005,3006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 티나비추기(self.ctx)


# 티나비추기
class 티나비추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera(trigger_id=3004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 티나대사1(self.ctx)


class 티나대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npc_id=11000136, illust_id='Tina_normal', msg='$52020036_QD__MAIN__4$', duration=5000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 몬스터한번더스폰(self.ctx)


class 몬스터한번더스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[20001], auto_target=False)
        self.spawn_monster(spawn_ids=[10000], auto_target=False)
        self.spawn_monster(spawn_ids=[10001], auto_target=False)
        self.spawn_monster(spawn_ids=[10002], auto_target=False)
        self.spawn_monster(spawn_ids=[10003], auto_target=False)
        self.spawn_monster(spawn_ids=[10004], auto_target=False)
        self.spawn_monster(spawn_ids=[10005], auto_target=False)
        self.spawn_monster(spawn_ids=[10006], auto_target=False)
        self.spawn_monster(spawn_ids=[10007], auto_target=False)
        self.spawn_monster(spawn_ids=[10008], auto_target=False)
        self.spawn_monster(spawn_ids=[10010], auto_target=False)
        self.spawn_monster(spawn_ids=[10012], auto_target=False)
        self.spawn_monster(spawn_ids=[10014], auto_target=False)
        self.spawn_monster(spawn_ids=[10016], auto_target=False)
        self.spawn_monster(spawn_ids=[10016], auto_target=False)
        self.spawn_monster(spawn_ids=[10017], auto_target=False)
        self.spawn_monster(spawn_ids=[10018], auto_target=False)
        self.spawn_monster(spawn_ids=[10019], auto_target=False)
        self.spawn_monster(spawn_ids=[10020], auto_target=False)
        self.spawn_monster(spawn_ids=[10021], auto_target=False)
        self.spawn_monster(spawn_ids=[10022], auto_target=False)
        self.spawn_monster(spawn_ids=[10023], auto_target=False)
        self.spawn_monster(spawn_ids=[10024], auto_target=False)
        self.spawn_monster(spawn_ids=[10025], auto_target=False)
        self.spawn_monster(spawn_ids=[10026], auto_target=False)
        self.spawn_monster(spawn_ids=[10027], auto_target=False)
        self.spawn_monster(spawn_ids=[10028], auto_target=False)
        self.spawn_monster(spawn_ids=[10029], auto_target=False)
        self.spawn_monster(spawn_ids=[10030], auto_target=False)
        self.spawn_monster(spawn_ids=[10031], auto_target=False)
        self.spawn_monster(spawn_ids=[10032], auto_target=False)
        self.spawn_monster(spawn_ids=[10033], auto_target=False)
        self.spawn_monster(spawn_ids=[10034], auto_target=False)
        self.spawn_monster(spawn_ids=[10035], auto_target=False)
        self.spawn_monster(spawn_ids=[10036], auto_target=False)
        self.spawn_monster(spawn_ids=[10037], auto_target=False)
        self.spawn_monster(spawn_ids=[10038], auto_target=False)
        self.spawn_monster(spawn_ids=[10039], auto_target=False)
        self.spawn_monster(spawn_ids=[10040], auto_target=False)
        self.spawn_monster(spawn_ids=[10041], auto_target=False)
        self.spawn_monster(spawn_ids=[10042], auto_target=False)
        self.spawn_monster(spawn_ids=[10043], auto_target=False)
        self.spawn_monster(spawn_ids=[10044], auto_target=False)
        self.spawn_monster(spawn_ids=[10045], auto_target=False)
        self.spawn_monster(spawn_ids=[10046], auto_target=False)
        self.spawn_monster(spawn_ids=[10047], auto_target=False)
        self.spawn_monster(spawn_ids=[10048], auto_target=False)
        self.spawn_monster(spawn_ids=[10049], auto_target=False)
        self.spawn_monster(spawn_ids=[10050], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 부상자구하기시작(self.ctx)


class 부상자구하기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 부상자구출퀘스트완료체크(self.ctx)


class 부상자구출퀘스트완료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000048], quest_states=[2]):
            return 부상자옮기기대사(self.ctx)


# 티나 팝업 대사 UI_1
class 부상자옮기기대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_quest_complete(quest_id=91000048)
        self.set_quest_accept(quest_id=91000049)
        self.side_npc_talk(npc_id=11003780, illust='WhitewolfGirl_normal', duration=5648, script='$52020036_QD__main__14$', voice='ko/Npc/00002151')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5648):
            return 네이린팝업1(self.ctx)


# 네이린팝업1
class 네이린팝업1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=7000, script='$52020036_QD__main__15$', voice='ko/Npc/00002126')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 네이린팝업2(self.ctx)


class 네이린팝업2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_smile', duration=7000, script='$52020036_QD__main__16$', voice='ko/Npc/00002127')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 네이린팝업3(self.ctx)


class 네이린팝업3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=7000, script='$52020036_QD__main__17$', voice='ko/Npc/00002128')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 공중지원퀘스트자동수락(self.ctx)


class 공중지원퀘스트자동수락(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000043], state=1)
        self.destroy_monster(spawn_ids=[901])
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[201])
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 콘대르구르는천둥P3스폰(self.ctx)


class 콘대르구르는천둥P3스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[902], auto_target=False)
        self.spawn_monster(spawn_ids=[8000], auto_target=False)
        self.spawn_monster(spawn_ids=[8001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 석궁비추기(self.ctx)


# 석궁비추기
class 석궁비추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=3007)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 석궁비추기끝(self.ctx)


class 석궁비추기끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 콘대르팝업1(self.ctx)


class 콘대르팝업1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003776, illust='Conder_normal', duration=7000, script='$52020036_QD__main__18$', voice='ko/Npc/00002148')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 네이린팝업4(self.ctx)


class 네이린팝업4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_shy', duration=7000, script='$52020036_QD__main__19$', voice='ko/Npc/00002129')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 콘대르팝업2(self.ctx)


class 콘대르팝업2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003776, illust='Conder_normal', duration=6000, script='$52020036_QD__main__20$', voice='ko/Npc/00002149')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 네이린웨이브경고팝업(self.ctx)


class 네이린웨이브경고팝업(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=1000, script='$52020036_QD__main__21$', voice='ko/Npc/00002130')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1340):
            return 네이린웨이브경고팝업1(self.ctx)


class 네이린웨이브경고팝업1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=7000, script='$52020036_QD__main__22$', voice='ko/Npc/00002131')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7012):
            return 네이린웨이브경고팝업2(self.ctx)


class 네이린웨이브경고팝업2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 웨이브스폰1(self.ctx)


class 웨이브스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10051], auto_target=False)
        self.spawn_monster(spawn_ids=[10059], auto_target=False)
        self.spawn_monster(spawn_ids=[10067], auto_target=False)
        self.spawn_monster(spawn_ids=[10075], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 웨이브스폰1패트롤(self.ctx)


class 웨이브스폰1패트롤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10051, patrol_name='WavePatrolDataEast')
        self.move_npc(spawn_id=10059, patrol_name='WavePatrolDataEast')
        self.move_npc(spawn_id=10067, patrol_name='WavePatrolDataWest')
        self.move_npc(spawn_id=10075, patrol_name='WavePatrolDataSouth')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 웨이브스폰2(self.ctx) # 웨이브스폰2 / 공중지원퀘스트완료체크


class 웨이브스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10055], auto_target=False)
        self.spawn_monster(spawn_ids=[10063], auto_target=False)
        self.spawn_monster(spawn_ids=[10071], auto_target=False)
        self.spawn_monster(spawn_ids=[10079], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 웨이브스폰3(self.ctx)


class 웨이브스폰3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10052], auto_target=False)
        self.spawn_monster(spawn_ids=[10060], auto_target=False)
        self.spawn_monster(spawn_ids=[10068], auto_target=False)
        self.spawn_monster(spawn_ids=[10076], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 웨이브스폰4(self.ctx)


class 웨이브스폰4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10056], auto_target=False)
        self.spawn_monster(spawn_ids=[10064], auto_target=False)
        self.spawn_monster(spawn_ids=[10072], auto_target=False)
        self.spawn_monster(spawn_ids=[10080], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 웨이브스폰5(self.ctx)


class 웨이브스폰5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10053], auto_target=False)
        self.spawn_monster(spawn_ids=[10061], auto_target=False)
        self.spawn_monster(spawn_ids=[10069], auto_target=False)
        self.spawn_monster(spawn_ids=[10078], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 웨이브스폰6(self.ctx)


class 웨이브스폰6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10054], auto_target=False)
        self.spawn_monster(spawn_ids=[10057], auto_target=False)
        self.spawn_monster(spawn_ids=[10065], auto_target=False)
        self.spawn_monster(spawn_ids=[10073], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 웨이브스폰7(self.ctx)


class 웨이브스폰7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10058], auto_target=False)
        self.spawn_monster(spawn_ids=[10062], auto_target=False)
        self.spawn_monster(spawn_ids=[10066], auto_target=False)
        self.spawn_monster(spawn_ids=[10070], auto_target=False)
        self.spawn_monster(spawn_ids=[10074], auto_target=False)
        self.spawn_monster(spawn_ids=[10077], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차웨이브스폰1_2(self.ctx)


class 차웨이브스폰1_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10051], auto_target=False)
        self.spawn_monster(spawn_ids=[10059], auto_target=False)
        self.spawn_monster(spawn_ids=[10067], auto_target=False)
        self.spawn_monster(spawn_ids=[10075], auto_target=False)
        self.spawn_monster(spawn_ids=[10079], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차웨이브스폰2_2(self.ctx)


class 차웨이브스폰2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10052], auto_target=False)
        self.spawn_monster(spawn_ids=[10055], auto_target=False)
        self.spawn_monster(spawn_ids=[10060], auto_target=False)
        self.spawn_monster(spawn_ids=[10063], auto_target=False)
        self.spawn_monster(spawn_ids=[10071], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차웨이브스폰3_2(self.ctx)


class 차웨이브스폰3_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10056], auto_target=False)
        self.spawn_monster(spawn_ids=[10064], auto_target=False)
        self.spawn_monster(spawn_ids=[10068], auto_target=False)
        self.spawn_monster(spawn_ids=[10072], auto_target=False)
        self.spawn_monster(spawn_ids=[10076], auto_target=False)
        self.spawn_monster(spawn_ids=[10080], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차웨이브스폰4_2(self.ctx)


class 차웨이브스폰4_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10053], auto_target=False)
        self.spawn_monster(spawn_ids=[10057], auto_target=False)
        self.spawn_monster(spawn_ids=[10061], auto_target=False)
        self.spawn_monster(spawn_ids=[10065], auto_target=False)
        self.spawn_monster(spawn_ids=[10069], auto_target=False)
        self.spawn_monster(spawn_ids=[10073], auto_target=False)
        self.spawn_monster(spawn_ids=[10078], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차웨이브스폰5_2(self.ctx)


class 차웨이브스폰5_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10054], auto_target=False)
        self.spawn_monster(spawn_ids=[10058], auto_target=False)
        self.spawn_monster(spawn_ids=[10062], auto_target=False)
        self.spawn_monster(spawn_ids=[10066], auto_target=False)
        self.spawn_monster(spawn_ids=[10070], auto_target=False)
        self.spawn_monster(spawn_ids=[10074], auto_target=False)
        self.spawn_monster(spawn_ids=[10077], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 공중지원퀘스트완료체크(self.ctx)


class 공중지원퀘스트완료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000049], quest_states=[2]):
            return 공중지원퀘스트완료(self.ctx)


class 공중지원퀘스트완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000043], state=0)
        self.visible_my_pc(is_visible=False) # 캐릭터 숨김
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawn_ids=[-1])
        self.set_quest_complete(quest_id=91000049)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엔딩크림슨발록보이는위치로유저이동(self.ctx)


class 엔딩크림슨발록보이는위치로유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020036, portal_id=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩크림슨발록비추기(self.ctx)


class 엔딩크림슨발록비추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=3015)
        self.spawn_monster(spawn_ids=[7000], auto_target=False)
        self.spawn_monster(spawn_ids=[7001], auto_target=False)
        self.spawn_monster(spawn_ids=[7002], auto_target=False)
        self.spawn_monster(spawn_ids=[7003], auto_target=False)
        self.spawn_monster(spawn_ids=[7004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 크림슨발록엔딩닝대사(self.ctx)


class 크림슨발록엔딩닝대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=9000, skill_id=99910150)
        self.add_cinematic_talk(npc_id=11003781, msg='$52020036_QD__MAIN__5$', duration=5000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=7000, sequence_name='Attack_01_A', duration_tick=1900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 엔딩연출준비(self.ctx)


class 엔딩연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[7000])
        self.destroy_monster(spawn_ids=[7001])
        self.destroy_monster(spawn_ids=[7002])
        self.destroy_monster(spawn_ids=[7003])
        self.destroy_monster(spawn_ids=[7004])
        self.set_mesh(trigger_ids=[9999]) # 발록 함선 지우기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 엔딩연출1(self.ctx)


class 엔딩연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True) # 캐릭터 보임
        self.spawn_monster(spawn_ids=[3500], auto_target=False)
        self.spawn_monster(spawn_ids=[4500], auto_target=False)
        self.spawn_monster(spawn_ids=[5500], auto_target=False)
        self.set_scene_skip(state=전부지우기, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 엔딩카메라1(self.ctx)


class 엔딩카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3008)
        self.move_user(map_id=52020036, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 콘대르엔딩대사1(self.ctx)


class 콘대르엔딩대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003776, illust_id='Conder_normal', msg='$52020036_QD__MAIN__6$', duration=4000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 구르는천둥엔딩대사1(self.ctx)


class 구르는천둥엔딩대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003779, illust_id='LoudFist_normal', msg='$52020036_QD__MAIN__7$', duration=4000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 트리스탄생성1(self.ctx)


class 트리스탄생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[6500], auto_target=False)
        self.move_user(map_id=52020036, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 트리스탄등장카메라1(self.ctx)


class 트리스탄등장카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3009)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리스탄대사1(self.ctx)


class 트리스탄대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001975, illust_id='Tristan_normal', msg='$52020036_QD__MAIN__8$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 콘대르엔딩카메라1(self.ctx)


class 콘대르엔딩카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 콘대르엔딩카메라2(self.ctx)


class 콘대르엔딩카메라2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 콘대르엔딩대사2(self.ctx)


class 콘대르엔딩대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003776, illust_id='Conder_normal', msg='$52020036_QD__MAIN__9$', duration=1000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 콘대르엔딩카메라3(self.ctx)


class 콘대르엔딩카메라3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3012)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 콘대르엔딩대사3(self.ctx)


class 콘대르엔딩대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003776, illust_id='Conder_normal', msg='$52020036_QD__MAIN__10$', duration=2000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=3500, sequence_name='Bore_A', duration_tick=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 트리스탄엔딩카메라2(self.ctx)


class 트리스탄엔딩카메라2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3009)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리스탄엔딩대사2(self.ctx)


class 트리스탄엔딩대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003777, illust_id='Tristan_normal', msg='$52020036_QD__MAIN__11$', duration=4000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=6500, sequence_name='Talk_A', duration_tick=7000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 엔딩카메라2(self.ctx)


class 엔딩카메라2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3007,3016], return_view=False)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전부지우기(self.ctx)


class 전부지우기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52010052, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return None # Missing State: State


initial_state = 딜레이
