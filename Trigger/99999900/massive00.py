""" trigger/99999900/massive00.xml """
import trigger_api


# 트랩마스터
class 재생버튼(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg1은 상태그룹의 ID, arg2 상태그룹에 포함되는 상태이름들, arg3 0이면 순서대로 1이면 상태그룹을 랜덤하게 섞는다.
        # self.set_state(id=1, states=[퍼즐패턴10,퍼즐패턴11,퍼즐패턴12,퍼즐패턴13,퍼즐패턴14,퍼즐패턴15,퍼즐패턴16,퍼즐패턴17,퍼즐패턴18,퍼즐패턴19,퍼즐패턴20,퍼즐패턴21,퍼즐패턴22,퍼즐패턴23,퍼즐패턴24,퍼즐패턴25,퍼즐패턴26,퍼즐패턴27,퍼즐패턴28,퍼즐패턴29,퍼즐패턴30,퍼즐패턴31,퍼즐패턴32,퍼즐패턴33,퍼즐패턴34,퍼즐패턴35,퍼즐패턴36,퍼즐패턴37,퍼즐패턴38,퍼즐패턴39,퍼즐패턴40,퍼즐패턴41,퍼즐패턴42,퍼즐패턴43,퍼즐패턴44], randomize=True)
        self.set_event_ui(type=1, arg2='$99999900__MASSIVE00__0$', arg3='3000')
        self.set_event_ui(type=1, arg2='$99999900__MASSIVE00__1$', arg3='5000', arg4='0')
        self.set_timer(timer_id='1001', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 중지버튼(self.ctx)
        if self.user_detected(box_ids=[900]):
            return 일부패턴시작(self.ctx)
        if self.user_detected(box_ids=[902]):
            return 모든패턴순차시작(self.ctx)
        if self.user_detected(box_ids=[903]):
            return 모든패턴랜덤시작(self.ctx)
        if self.time_expired(timer_id='1001'):
            return 재생버튼(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1001')


class 일부패턴시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_state(id=1, states=[퍼즐패턴45,퍼즐패턴46,퍼즐패턴47,퍼즐패턴48,퍼즐패턴49,퍼즐패턴50,퍼즐패턴51,퍼즐패턴52,퍼즐패턴53,퍼즐패턴54,퍼즐패턴55,퍼즐패턴56,퍼즐패턴57,퍼즐패턴58,퍼즐패턴59,퍼즐패턴60])
        self.show_count_ui(text='$99999900__MASSIVE00__2$', stage=1, count=5)
        self.set_timer(timer_id='1002', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1002'):
            return 퍼즐단계(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1002')


class 모든패턴순차시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_state(id=1, states=[퍼즐패턴10,퍼즐패턴11,퍼즐패턴12,퍼즐패턴13,퍼즐패턴14,퍼즐패턴15,퍼즐패턴16,퍼즐패턴17,퍼즐패턴18,퍼즐패턴19,퍼즐패턴20,퍼즐패턴21,퍼즐패턴22,퍼즐패턴23,퍼즐패턴24,퍼즐패턴25,퍼즐패턴26,퍼즐패턴27,퍼즐패턴28,퍼즐패턴29,퍼즐패턴30,퍼즐패턴31,퍼즐패턴32,퍼즐패턴33,퍼즐패턴34,퍼즐패턴35,퍼즐패턴36,퍼즐패턴37,퍼즐패턴38,퍼즐패턴39,퍼즐패턴40,퍼즐패턴41,퍼즐패턴42,퍼즐패턴43,퍼즐패턴44,퍼즐패턴45,퍼즐패턴46,퍼즐패턴47,퍼즐패턴48,퍼즐패턴49,퍼즐패턴50,퍼즐패턴51,퍼즐패턴52,퍼즐패턴53,퍼즐패턴54,퍼즐패턴55,퍼즐패턴56,퍼즐패턴57,퍼즐패턴58,퍼즐패턴59,퍼즐패턴60])
        self.show_count_ui(text='$99999900__MASSIVE00__3$', stage=1, count=5)
        self.set_timer(timer_id='1003', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1003'):
            return 퍼즐단계(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1003')


class 모든패턴랜덤시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_state(id=1, states=[퍼즐패턴10,퍼즐패턴11,퍼즐패턴12,퍼즐패턴13,퍼즐패턴14,퍼즐패턴15,퍼즐패턴16,퍼즐패턴17,퍼즐패턴18,퍼즐패턴19,퍼즐패턴20,퍼즐패턴21,퍼즐패턴22,퍼즐패턴23,퍼즐패턴24,퍼즐패턴25,퍼즐패턴26,퍼즐패턴27,퍼즐패턴28,퍼즐패턴29,퍼즐패턴30,퍼즐패턴31,퍼즐패턴32,퍼즐패턴33,퍼즐패턴34,퍼즐패턴35,퍼즐패턴36,퍼즐패턴37,퍼즐패턴38,퍼즐패턴39,퍼즐패턴40,퍼즐패턴41,퍼즐패턴42,퍼즐패턴43,퍼즐패턴44,퍼즐패턴45,퍼즐패턴46,퍼즐패턴47,퍼즐패턴48,퍼즐패턴49,퍼즐패턴50,퍼즐패턴51,퍼즐패턴52,퍼즐패턴53,퍼즐패턴54,퍼즐패턴55,퍼즐패턴56,퍼즐패턴57,퍼즐패턴58,퍼즐패턴59,퍼즐패턴60], randomize=True)
        self.show_count_ui(text='$99999900__MASSIVE00__4$', stage=1, count=5)
        self.set_timer(timer_id='1004', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1004'):
            return 퍼즐단계(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1004')


class 퍼즐단계대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1005', seconds=5)
        self.set_event_ui(type=1, arg2='$99999900__MASSIVE00__5$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1005'):
            return 퍼즐단계(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1005')


class 퍼즐단계(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_timer(timer_id='99', seconds=14)
        self.use_state(id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 퍼즐단계정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='99')


class 퍼즐단계정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계종료(self.ctx)
        if self.user_detected(box_ids=[901]):
            return 중지버튼(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999900__MASSIVE00__6$', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[901]):
            return 퍼즐단계대기(self.ctx)


class 중지버튼(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999900__MASSIVE00__7$', arg3='5000')
        self.set_timer(timer_id='1000', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1000'):
            return 재생버튼(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1000')


"""
퍼즐 패턴 시작
9시->12시 방향 패턴
9시->12시 방향, 한줄씩 사라지는 패턴
"""
class 퍼즐패턴10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90], interval=100)


# 9시->12시 방향, 바깥에서 소용돌이로 빠지는 패턴
class 퍼즐패턴11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22,23,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,34,35,36,37,47,57,67,66,65,64,54,44], interval=100)


# 9시->12시 방향, 숫자 2 모양으로 한줄씩 남기고 사라지는 패턴
class 퍼즐패턴12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,20,30,29,28,27,26,25,24,23,22,21,31,41,42,43,44,45,46,47,48,49,50,60,70,69,68,67,66,65,64,63,62,61,71,81,82,83,84,85,86,87,88,89,90,100], interval=100)


# 9시->12시 방향, 3시->6시 방향, 각각 한 방향에서 한줄씩 사라짐.
class 퍼즐패턴13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,100,99,98,97,96,95,94,93,92,91,11,12,13,14,15,16,17,18,19,20,90,89,88,87,86,85,84,83,82,81,21,22,23,24,25,26,27,28,29,30,80,79,78,77,76,75,74,73,72,71,31,32,33,34,35,36,37,38,39,40,70,69,68,67,66,65,64,63,62,61], interval=100)


# 9시->12시 방향, 3시->6시 방향, 각각 한 방향에서 한줄씩 건너띄면서 한줄 씩 사라짐
class 퍼즐패턴14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,100,99,98,97,96,95,94,93,92,91,21,22,23,24,25,26,27,28,29,30,80,79,78,77,76,75,74,73,72,71,41,42,43,44,45,46,47,48,49,50,60,59,58,57,56,55,54,53,52,51], interval=100)


# 9시->12시 방향, 바깥쪽에서 원 1개씩 사라짐, 중간에 1줄씩 건너뛰면서 원을 그리며 사라짐
class 퍼즐패턴15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11], interval=100)
        self.set_mesh(trigger_ids=[23,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[45,46,55,56], start_delay=5600, interval=100)


# 9시->12시 방향, 12시->6시방향, 6시->3시 방향, 3시->9시 방향, 9시->6시방향, 그 후 시계 반대방향으로 원을 그림
class 퍼즐패턴16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,19,28,37,46,55,64,73,82,91,92,93,94,95,96,97,98,99,100,89,78,67,56,45,34,23,12,11,21,31,41,51,61,71,81,83,84,85,86,87,88,90,80,70,60,50,40,30,20,18,17,16,15,14,13,22,32,42,52,62,72,74,75,76,77,79,69,59,49,39,29,27,26,25,24], interval=100)


# 9시->12시 방향, 12시->6시방향, 6시->3시 방향, Z형태가 된 후 안쪽으로 원을 그리며 사라짐
class 퍼즐패턴17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,19,28,37,46,55,64,73,82,91,92,93,94,95,96,97,98,99,100,90,80,70,60,50,40,30,20,18,17,16,15,14,13,12,11,21,31,41,51,61,71,81,83,84,85,86,87,88,89,79,69,59,49,39,29,27,26,25,24,23,22,32,42,52,62,72,74,75,76,77,78,68,58,48,38,36,35,34,33,43,53,63,65,66,67], interval=100)


# 9시->12시 방향, 순서대로 S자로 사라지다가 다시 생겨남
class 퍼즐패턴18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,20,19,18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28,29,30,40,39,38,37,36,35,34,33,32,31,41,42,43,44,45,46,47,48,49,50,60,59,58,57,56,55,54,53,52,51,61,62,63,64,65,66,67,68,69,70,80,79,78,77,76,75,74,73,72,71,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], interval=100)
        self.set_mesh(trigger_ids=[10,9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19,20,30,29,28,27,26,25,24,23,22,21,31,32,33,34,35,36,37,38,39,40,50,49,48,47,46,45,44,43,42,41,51,52,53,54,55,56,57,58,59,60,70,69,68,67,66,65,64,63,62,61,71,72,73,74,75,76,77,78,79,80,90,89,88,87,86,85,84,83,82,81,91,92,93,94,95,96,97,98,99,100], visible=True, start_delay=1200, interval=100)


"""
9시->12시 방향과 12시->9시방향 중앙 동시 패턴
9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 S자로 차례대로 사라지는 패턴
"""
class 퍼즐패턴19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11], interval=100)
        self.set_mesh(trigger_ids=[60,59,58,57,56,55,54,53,52,51,61,62,63,64,65,66,67,68,69,70,80,79,78,77,76,75,74,73,72,71,81,82,83,84,85,86,87,88,89,90], interval=100)


# 9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 서로 원을 그리며 사라지는 패턴
class 퍼즐패턴20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[41,42,43,44,45,46,47,48,49,50,40,30,20,10,9,8,7,6,5,4,3,2,1,11,21,31,32,33,34,35,36,37,38,39,29,19,18,17,16,15,14,13,12,22], interval=100)
        self.set_mesh(trigger_ids=[60,59,58,57,56,55,54,53,52,51,61,71,81,91,92,93,94,95,96,97,98,99,100,90,80,70,69,68,67,66,65,64,63,62,72,82,83,84,85,86,87,88,89,79], interval=100)


# 9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 각각 12시, 3시 방향으로 반으로 나뉜 공간을 작은 S자 형태로 없앰
class 퍼즐패턴21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[41,42,43,44,45,46,47,48,49,50,40,30,20,10,9,19,29,39,38,28,18,8,7,17,27,37,36,26,16,6,5,15,25,35,34,24,14,4,3,13,23,33,32,22,12,2], interval=100)
        self.set_mesh(trigger_ids=[60,59,58,57,56,55,54,53,52,51,61,71,81,91,92,82,72,62,63,73,83,93,94,84,74,64,65,75,85,95,96,86,76,66,67,77,87,97,98,88,78,68,69,79,89,99], interval=100)


# 9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 각각 12시, 3시 방향으로 반으로 나뉜 공간을 큰 S자 형태로 없앰
class 퍼즐패턴22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[41,42,43,44,45,46,47,48,49,50,40,30,20,10,9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19,29,28,27,26,25,24,23,22,21,31], interval=100)
        self.set_mesh(trigger_ids=[60,59,58,57,56,55,54,53,52,51,61,71,81,91,92,93,94,95,96,97,98,99,100,90,89,88,87,86,85,84,83,82,72,73,74,75,76,77,78,79,80,70], interval=100)


# 9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 각각 끝과 안쪽이 차례대로 한줄씩 사라짐
class 퍼즐패턴23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[41,42,43,44,45,46,47,48,49,50,1,2,3,4,5,6,7,8,9,10,31,32,33,34,35,36,37,38,39,40,11,12,13,14,15,16,17,18,19,20], interval=100)
        self.set_mesh(trigger_ids=[60,59,58,57,56,55,54,53,52,51,100,99,98,97,96,95,94,93,92,91,70,69,68,67,66,65,64,63,62,61,90,89,88,87,86,85,84,83,82,81], interval=100)


# 9시->12시 방향과 12시->9시방향 중앙 동시, 한줄씩 사라지면서 다시 생성됨
class 퍼즐패턴24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[41,42,43,44,45,46,47,48,49,50,31,32,33,34,35,36,37,38,39,40,21,22,23,24,25,26,27,28,29,30,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10], interval=100)
        self.set_mesh(trigger_ids=[50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1], visible=True, start_delay=1200, interval=100)
        self.set_mesh(trigger_ids=[60,59,58,57,56,55,54,53,52,51,70,69,68,67,66,65,64,63,62,61,80,79,78,77,76,75,74,73,72,71,90,89,88,87,86,85,84,83,82,81,100,99,98,97,96,95,94,93,92,91], interval=100)
        self.set_mesh(trigger_ids=[51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True, start_delay=1200, interval=100)


"""
같은 색상 별로 띄엄띄엄 사라짐 패턴
같은 색상 별로 띄엄띄엄 사라짐, 12시 방향에서 6시 방향으로 노란색이 사라짐
"""
class 퍼즐패턴25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_timer(timer_id='1', seconds=10)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[8,19,30], start_delay=500)
        self.set_mesh(trigger_ids=[6,17,28,39,50], start_delay=1000)
        self.set_mesh(trigger_ids=[4,15,26,37,48,59,70], start_delay=1500)
        self.set_mesh(trigger_ids=[2,13,24,35,46,57,68,79,90], start_delay=2000)
        self.set_mesh(trigger_ids=[11,22,33,44,55,66,77,88,99], start_delay=2500)
        self.set_mesh(trigger_ids=[31,42,53,64,75,86,97], start_delay=3000)
        self.set_mesh(trigger_ids=[51,62,73,84,95], start_delay=3500)
        self.set_mesh(trigger_ids=[71,82,93], start_delay=4000)
        self.set_mesh(trigger_ids=[91], start_delay=4500)


# 같은 색상 별로 띄엄띄엄 사라짐, 12시->3시 방향의 가로가 사라짐, 노란색이 사라지다가, 중간부터 반대편의 흰색이 사라짐
class 퍼즐패턴26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10,30,50,70,90])
        self.set_mesh(trigger_ids=[19,39,59,79,99], start_delay=500)
        self.set_mesh(trigger_ids=[8,28,48,68,88], start_delay=1000)
        self.set_mesh(trigger_ids=[17,37,57,77,97], start_delay=1500)
        self.set_mesh(trigger_ids=[6,26,46,66,86], start_delay=2000)
        self.set_mesh(trigger_ids=[1,21,41,61,81], start_delay=2500)
        self.set_mesh(trigger_ids=[12,32,52,72,92], start_delay=3000)
        self.set_mesh(trigger_ids=[3,23,43,63,83], start_delay=3500)
        self.set_mesh(trigger_ids=[14,34,54,74,94], start_delay=4000)
        self.set_mesh(trigger_ids=[5,25,45,65,85], start_delay=4500)


# 같은 색상 별로 띄엄띄엄 사라짐, 12시->3시 방향의 가로가 사라짐, 노란색이 차례대로 계속 사라짐
class 퍼즐패턴27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10,30,50,70,90])
        self.set_mesh(trigger_ids=[19,39,59,79,99], start_delay=500)
        self.set_mesh(trigger_ids=[8,28,48,68,88], start_delay=1000)
        self.set_mesh(trigger_ids=[17,37,57,77,97], start_delay=1500)
        self.set_mesh(trigger_ids=[6,26,46,66,86], start_delay=2000)
        self.set_mesh(trigger_ids=[15,35,55,75,95], start_delay=2500)
        self.set_mesh(trigger_ids=[4,24,44,64,84], start_delay=3000)
        self.set_mesh(trigger_ids=[13,33,53,73,93], start_delay=3500)
        self.set_mesh(trigger_ids=[2,22,42,62,82], start_delay=4000)
        self.set_mesh(trigger_ids=[11,31,51,71,91], start_delay=4500)


"""
12시 방향에서 쭉 내려오는 패턴
12시 방향에서 쭉 내려오는 패턴, 한 줄로 사라지면서 다시 나타나는 패턴
"""
class 퍼즐패턴28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[9,20], start_delay=500)
        self.set_mesh(trigger_ids=[8,19,30], start_delay=1000)
        self.set_mesh(trigger_ids=[7,18,29,40], start_delay=1500)
        self.set_mesh(trigger_ids=[6,17,28,39,50], start_delay=2000)
        self.set_mesh(trigger_ids=[5,16,27,38,49,60], start_delay=2500)
        self.set_mesh(trigger_ids=[4,15,26,37,48,59,70], start_delay=3000)
        self.set_mesh(trigger_ids=[3,14,25,36,47,58,69,80], start_delay=3500)
        self.set_mesh(trigger_ids=[2,13,24,35,46,57,68,79,90], start_delay=4000)
        self.set_mesh(trigger_ids=[1,12,23,34,45,56,67,78,89,100], start_delay=4500)
        self.set_mesh(trigger_ids=[11,22,33,44,55,66,77,88,99], start_delay=5000)
        self.set_mesh(trigger_ids=[21,32,43,54,65,76,87,98], start_delay=5500)
        self.set_mesh(trigger_ids=[31,42,53,64,75,86,97], start_delay=6000)
        self.set_mesh(trigger_ids=[41,52,63,74,85,96], start_delay=6500)
        self.set_mesh(trigger_ids=[51,62,73,84,95], start_delay=7000)
        self.set_mesh(trigger_ids=[61,72,83,94], start_delay=7500)
        self.set_mesh(trigger_ids=[71,82,93], start_delay=8000)
        self.set_mesh(trigger_ids=[81,92], start_delay=8500)
        self.set_mesh(trigger_ids=[91], start_delay=9000)
        self.set_mesh(trigger_ids=[10], visible=True, start_delay=1500)
        self.set_mesh(trigger_ids=[9,20], visible=True, start_delay=2000)
        self.set_mesh(trigger_ids=[8,19,30], visible=True, start_delay=2500)
        self.set_mesh(trigger_ids=[7,18,29,40], visible=True, start_delay=3000)
        self.set_mesh(trigger_ids=[6,17,28,39,50], visible=True, start_delay=3500)
        self.set_mesh(trigger_ids=[5,16,27,38,49,60], visible=True, start_delay=4000)
        self.set_mesh(trigger_ids=[4,15,26,37,48,59,70], visible=True, start_delay=4500)
        self.set_mesh(trigger_ids=[3,14,25,36,47,58,69,80], visible=True, start_delay=5000)
        self.set_mesh(trigger_ids=[2,13,24,35,46,57,68,79,90], visible=True, start_delay=5500)
        self.set_mesh(trigger_ids=[1,12,23,34,45,56,67,78,89,100], visible=True, start_delay=6000)
        self.set_mesh(trigger_ids=[11,22,33,44,55,66,77,88,99], visible=True, start_delay=6500)
        self.set_mesh(trigger_ids=[21,32,43,54,65,76,87,98], visible=True, start_delay=7000)
        self.set_mesh(trigger_ids=[31,42,53,64,75,86,97], visible=True, start_delay=7500)
        self.set_mesh(trigger_ids=[41,52,63,74,85,96], visible=True, start_delay=8000)
        self.set_mesh(trigger_ids=[51,62,73,84,95], visible=True, start_delay=8500)
        self.set_mesh(trigger_ids=[61,72,83,94], visible=True, start_delay=9000)
        self.set_mesh(trigger_ids=[71,82,93], visible=True, start_delay=9500)
        self.set_mesh(trigger_ids=[81,92], visible=True, start_delay=10000)
        self.set_mesh(trigger_ids=[91], visible=True, start_delay=10500)


# 12시 방향에서 쭉 내려오는 패턴, 12시 방향에서 내려오고 동시에 6시 방향에서 올라오면서 가운데 대각선만 남기는 패턴
class 퍼즐패턴29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[9,20], start_delay=500)
        self.set_mesh(trigger_ids=[8,19,30], start_delay=1000)
        self.set_mesh(trigger_ids=[7,18,29,40], start_delay=1500)
        self.set_mesh(trigger_ids=[6,17,28,39,50], start_delay=2000)
        self.set_mesh(trigger_ids=[5,16,27,38,49,60], start_delay=2500)
        self.set_mesh(trigger_ids=[4,15,26,37,48,59,70], start_delay=3000)
        self.set_mesh(trigger_ids=[3,14,25,36,47,58,69,80], start_delay=3500)
        self.set_mesh(trigger_ids=[2,13,24,35,46,57,68,79,90], start_delay=4000)
        self.set_mesh(trigger_ids=[11,22,33,44,55,66,77,88,99], start_delay=4000)
        self.set_mesh(trigger_ids=[21,32,43,54,65,76,87,98], start_delay=3500)
        self.set_mesh(trigger_ids=[31,42,53,64,75,86,97], start_delay=3000)
        self.set_mesh(trigger_ids=[41,52,63,74,85,96], start_delay=2500)
        self.set_mesh(trigger_ids=[51,62,73,84,95], start_delay=2000)
        self.set_mesh(trigger_ids=[61,72,83,94], start_delay=1500)
        self.set_mesh(trigger_ids=[71,82,93], start_delay=1000)
        self.set_mesh(trigger_ids=[81,92], start_delay=500)
        self.set_mesh(trigger_ids=[91])


# 12시 방향에서 쭉 내려오는 패턴, ㅅ자 형태로 사라짐
class 퍼즐패턴30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[9,8,7,6,5,4,3,2,1], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[20,30,40,50,60,70,80,90,100], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[19], start_delay=900)
        self.set_mesh(trigger_ids=[18,17,16,15,14,13,12,11], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[29,39,49,59,69,79,89,99], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[28], start_delay=1700)
        self.set_mesh(trigger_ids=[27,26,25,24,23,22,21], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[38,48,58,68,78,88,98], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[37], start_delay=2400)
        self.set_mesh(trigger_ids=[36,35,34,33,32,31], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[47,57,67,77,87,97], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[46], start_delay=3000)
        self.set_mesh(trigger_ids=[45,44,43,42,41], start_delay=3100, interval=100)
        self.set_mesh(trigger_ids=[56,66,76,86,96], start_delay=3100, interval=100)
        self.set_mesh(trigger_ids=[55], start_delay=3500)
        self.set_mesh(trigger_ids=[54,53,52,51], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[65,75,85,95], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[64], start_delay=3900)
        self.set_mesh(trigger_ids=[63,62,61], start_delay=4000, interval=100)
        self.set_mesh(trigger_ids=[74,84,94], start_delay=4000, interval=100)
        self.set_mesh(trigger_ids=[73], start_delay=4200)
        self.set_mesh(trigger_ids=[72,71], start_delay=4300, interval=100)
        self.set_mesh(trigger_ids=[83,93], start_delay=4300, interval=100)


# 12시 방향에서 쭉 내려오는 패턴, 12시 방향 및 6시 방향에서 번갈아서 ㅅ자 형태로 사라짐
class 퍼즐패턴31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[9,8,7,6,5,4,3,2,1], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[20,30,40,50,60,70,80,90,100], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[91], start_delay=900)
        self.set_mesh(trigger_ids=[81,71,61,51,41,31,21,11], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[92,93,94,95,96,97,98,99], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[19], start_delay=1700)
        self.set_mesh(trigger_ids=[18,17,16,15,14,13,12], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[29,39,49,59,69,79,89], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[82], start_delay=2400)
        self.set_mesh(trigger_ids=[72,62,52,42,32,22], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[83,84,85,86,87,88], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[28], start_delay=3000)
        self.set_mesh(trigger_ids=[27,26,25,24,23], start_delay=3100, interval=100)
        self.set_mesh(trigger_ids=[38,48,58,68,78], start_delay=3100, interval=100)
        self.set_mesh(trigger_ids=[73], start_delay=3500)
        self.set_mesh(trigger_ids=[63,53,43,33], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[74,75,76,77], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[37], start_delay=3900)
        self.set_mesh(trigger_ids=[36,35,34], start_delay=4000, interval=100)
        self.set_mesh(trigger_ids=[47,57,67], start_delay=4000, interval=100)
        self.set_mesh(trigger_ids=[64], start_delay=4200)
        self.set_mesh(trigger_ids=[54,44], start_delay=4300, interval=100)
        self.set_mesh(trigger_ids=[65,66], start_delay=4300, interval=100)


# 12시 방향에서 쭉 내려오는 패턴, 12시 방향 및 6시 방향에서 번갈아서 한줄 씩 띄우고 ㅅ자 형태로 사라짐
class 퍼즐패턴32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[9,8,7,6,5,4,3,2,1], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[20,30,40,50,60,70,80,90,100], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[91], start_delay=900)
        self.set_mesh(trigger_ids=[81,71,61,51,41,31,21,11], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[92,93,94,95,96,97,98,99], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[28], start_delay=1700)
        self.set_mesh(trigger_ids=[27,26,25,24,23,22], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[38,48,58,68,78,88], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[73], start_delay=2400)
        self.set_mesh(trigger_ids=[63,53,43,33,13], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[74,75,76,77,79], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[46], start_delay=3000)
        self.set_mesh(trigger_ids=[45,44,42], start_delay=3100, interval=100)
        self.set_mesh(trigger_ids=[56,66,86], start_delay=3100, interval=100)
        self.set_mesh(trigger_ids=[55], start_delay=3500)
        self.set_mesh(trigger_ids=[35,15], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[57,59], start_delay=3600, interval=100)


# 12시에서 3시 방향으로 큐브가 사라짐, 1시 방향에서 7시 방향으로 각 열마다 큐브 하나씩만 대각선으로 남기면서 없어지는 패턴
class 퍼즐패턴33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[20,30,40,50,60,70,80,90,100])
        self.set_mesh(trigger_ids=[9,29,39,49,59,69,79,89,99], start_delay=500)
        self.set_mesh(trigger_ids=[8,18,38,48,58,68,78,88,98], start_delay=1000)
        self.set_mesh(trigger_ids=[7,17,27,47,57,67,77,87,97], start_delay=1500)
        self.set_mesh(trigger_ids=[6,16,26,36,56,66,76,86,96], start_delay=2000)
        self.set_mesh(trigger_ids=[5,15,25,35,45,65,75,85,95], start_delay=2500)
        self.set_mesh(trigger_ids=[4,14,24,34,44,54,74,84,94], start_delay=3000)
        self.set_mesh(trigger_ids=[3,13,23,33,43,53,63,83,93], start_delay=3500)
        self.set_mesh(trigger_ids=[2,12,22,32,42,52,62,72,92], start_delay=4000)
        self.set_mesh(trigger_ids=[1,11,21,31,41,51,61,71,81], start_delay=4500)


"""
안쪽 사각형 부터 사라지는 패턴
안쪽 사각형 부터 사라지는 패턴, 안쪽부터 소용돌이 모양을 그리며 바깥쪽으로 빠지는 패턴
"""
class 퍼즐패턴34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[46,56,55,45,35,36,37,47,57,67,66,65,64,54,44,34,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,23,13,14,15,16,17,18,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22,12], interval=100)


# 안쪽 사각형 부터 사라지는 패턴, 안쪽부터 소용돌이 모양을 그리며 한 줄씩 띄우고 바깥쪽으로 빠지는 패턴
class 퍼즐패턴35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[46,56,55,45,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,23,24,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,1,2,3,4,5,6,7,8,9,10,20], interval=100)


# 안쪽 사각형 부터 사라지는 패턴, 안쪽부터 4개가 먼저 사라진 후 바깥쪽으로 이동하여 바깥쪽부터 원을 그리며 사라지는 패턴
class 퍼즐패턴36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[46,56,55,45,35,25,15,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22,23,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,34,35,36,37,47,57,67,66,65,64,54,44], interval=100)


# 안쪽 사각형 부터 사라지는 패턴, 안쪽부터 4개가 먼저 사라진 후 서로 마주보며 U자 형태로 사라짐
class 퍼즐패턴37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[46,56,55,45,64,54,44,34,35,36,37,47,57,67,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,23,82,72,62,52,42,32,22,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,1], interval=100)


"""
가운데서 사방으로 퍼져나가는 패턴
가운데서 사방으로 퍼져나가는 패턴, 가운데서 사방으로 퍼져가면서 v자 모양으로 사라짐
"""
class 퍼즐패턴38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[45,34,23,12,1], interval=200)
        self.set_mesh(trigger_ids=[46,37,28,19,10], interval=200)
        self.set_mesh(trigger_ids=[56,67,78,89,100], interval=200)
        self.set_mesh(trigger_ids=[55,64,73,82,91], interval=200)
        self.set_mesh(trigger_ids=[44,33,22,11], start_delay=1300, interval=200)
        self.set_mesh(trigger_ids=[35,24,13,2], start_delay=1300, interval=200)
        self.set_mesh(trigger_ids=[36,27,18,9], start_delay=1300, interval=200)
        self.set_mesh(trigger_ids=[47,38,29,20], start_delay=1300, interval=200)
        self.set_mesh(trigger_ids=[57,68,79,90], start_delay=1300, interval=200)
        self.set_mesh(trigger_ids=[66,77,88,99], start_delay=1300, interval=200)
        self.set_mesh(trigger_ids=[65,74,83,92], start_delay=1300, interval=200)
        self.set_mesh(trigger_ids=[54,63,72,81], start_delay=1300, interval=200)
        self.set_mesh(trigger_ids=[43,32,21], start_delay=2400, interval=200)
        self.set_mesh(trigger_ids=[25,14,3], start_delay=2400, interval=200)
        self.set_mesh(trigger_ids=[26,17,8], start_delay=2400, interval=200)
        self.set_mesh(trigger_ids=[48,39,30], start_delay=2400, interval=200)
        self.set_mesh(trigger_ids=[58,69,80], start_delay=2400, interval=200)
        self.set_mesh(trigger_ids=[76,87,98], start_delay=2400, interval=200)
        self.set_mesh(trigger_ids=[75,84,93], start_delay=2400, interval=200)
        self.set_mesh(trigger_ids=[53,62,71], start_delay=2400, interval=200)
        self.set_mesh(trigger_ids=[42,31], start_delay=3500, interval=200)
        self.set_mesh(trigger_ids=[15,4], start_delay=3500, interval=200)
        self.set_mesh(trigger_ids=[16,7], start_delay=3500, interval=200)
        self.set_mesh(trigger_ids=[49,40], start_delay=3500, interval=200)
        self.set_mesh(trigger_ids=[59,70], start_delay=3500, interval=200)
        self.set_mesh(trigger_ids=[86,97], start_delay=3500, interval=200)
        self.set_mesh(trigger_ids=[85,94], start_delay=3500, interval=200)
        self.set_mesh(trigger_ids=[52,61], start_delay=3500, interval=200)


# 가운데서 사방으로 퍼져나가는 패턴, 가운데서 사방으로 퍼져가면서 v자 모양으로 사라짐
class 퍼즐패턴39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[45])
        self.set_mesh(trigger_ids=[35,25,15,5], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[44,43,42,41], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[46])
        self.set_mesh(trigger_ids=[36,26,16,6], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[47,48,49,50], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[56])
        self.set_mesh(trigger_ids=[57,58,59,60], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[66,76,86,96], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[55])
        self.set_mesh(trigger_ids=[65,75,85,95], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[54,53,52,51], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[64], start_delay=900)
        self.set_mesh(trigger_ids=[74,84,94], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[63,62,61], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[34], start_delay=900)
        self.set_mesh(trigger_ids=[33,32,31], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[24,14,4], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[37], start_delay=900)
        self.set_mesh(trigger_ids=[38,39,40], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[27,17,7], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[67], start_delay=900)
        self.set_mesh(trigger_ids=[77,87,97], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[68,69,70], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[73], start_delay=1700)
        self.set_mesh(trigger_ids=[83,93], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[72,71], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[23], start_delay=1700)
        self.set_mesh(trigger_ids=[22,21], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[13,3], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[28], start_delay=1700)
        self.set_mesh(trigger_ids=[18,8], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[29,30], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[78], start_delay=1700)
        self.set_mesh(trigger_ids=[79,80], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[88,98], start_delay=1800, interval=100)
        self.set_mesh(trigger_ids=[82], start_delay=2400)
        self.set_mesh(trigger_ids=[81], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[92], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[12], start_delay=2400)
        self.set_mesh(trigger_ids=[11], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[2], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[19], start_delay=2400)
        self.set_mesh(trigger_ids=[20], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[9], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[89], start_delay=2400)
        self.set_mesh(trigger_ids=[99], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[90], start_delay=2500, interval=100)


"""
12시->6시방향으로 사라짐
12시->6시방향으로 사라짐, 한 줄로 땅이 갈라진 후 바깥쪽으로 확대되는 패턴
"""
class 퍼즐패턴40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10,19,28,37,46,55,64,73,82,91], interval=100)
        self.set_mesh(trigger_ids=[9,18,27,36,45,54,63,72,81,20,29,38,47,56,65,74,83,92], start_delay=1000)
        self.set_mesh(trigger_ids=[8,17,26,35,44,53,62,71,30,39,48,57,66,75,84,93], start_delay=1500)
        self.set_mesh(trigger_ids=[7,16,25,34,43,52,61,40,49,58,67,76,85,94], start_delay=2000)
        self.set_mesh(trigger_ids=[6,15,24,33,42,51,50,59,68,77,86,95], start_delay=2500)
        self.set_mesh(trigger_ids=[5,14,23,32,41,60,69,78,87,96], start_delay=2500)
        self.set_mesh(trigger_ids=[4,13,22,31,70,79,88,97], start_delay=3000)
        self.set_mesh(trigger_ids=[3,12,21,80,89,98], start_delay=3500)
        self.set_mesh(trigger_ids=[2,11,90,99], start_delay=4000)


# 12시->6시방향으로 사라짐, 한 줄로 땅이 갈라진 후 바깥쪽으로 확대되는 패턴
class 퍼즐패턴41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10,19,28,37,46,55,64,73,82,91], interval=100)
        self.set_mesh(trigger_ids=[81,71,61,51,41,31,21,11,1,2,3,4,5,6,7,8,9,18,27,36,45,54,63,72,62,52,42,32,22,12,13,14,15,16,17,26,35,44,53,43,33,23], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[92,93,94,95,96,97,98,99,100,90,80,70,60,50,40,30,20,29,38,47,56,65,74,83,84,85,86,87,88,89,79,69,59,49,39,48,57,66,75,76,77,78], start_delay=1000, interval=100)


# 12시->6시방향으로 사라짐, 한 줄로 땅이 갈라진 후 안쪽으로 원을 만들면서 사라지는 패턴
class 퍼즐패턴42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10,19,28,37,46,55,64,73,82,91], interval=100)
        self.set_mesh(trigger_ids=[81,71,61,51,41,31,21,11,1,2,3,4,5,6,7,8,9,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,72,62,52,42,32,22,12,13,14,15,16,17,18,29,39,49,59,69,79,89,88,87,86,85,84,83,63,53,43,33,23,24,25,26,27,38,48,58,68,78,77,76,75,74,54,44,34,35,36,47,57,67,66,65], start_delay=1000, interval=100)


class 퍼즐패턴43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[91], start_delay=100)
        self.set_mesh(trigger_ids=[9,20], start_delay=200, interval=100)
        self.set_mesh(trigger_ids=[81,92], start_delay=400, interval=100)
        self.set_mesh(trigger_ids=[8,19,30], start_delay=600, interval=100)
        self.set_mesh(trigger_ids=[71,82,93], start_delay=900, interval=100)
        self.set_mesh(trigger_ids=[7,18,29,40], start_delay=1200, interval=100)
        self.set_mesh(trigger_ids=[61,72,83,94], start_delay=1600, interval=100)
        self.set_mesh(trigger_ids=[6,17,28,39,50], start_delay=2000, interval=100)
        self.set_mesh(trigger_ids=[51,62,73,84,95], start_delay=2500, interval=100)
        self.set_mesh(trigger_ids=[5,16,27,38,49,60], start_delay=3000, interval=100)
        self.set_mesh(trigger_ids=[41,52,63,74,85,96], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[4,15,26,37,48,59,70], start_delay=4200, interval=100)
        self.set_mesh(trigger_ids=[31,42,53,64,75,86,97], start_delay=4900, interval=100)
        self.set_mesh(trigger_ids=[3,14,25,36,47,58,69,80], start_delay=5600, interval=100)
        self.set_mesh(trigger_ids=[21,32,43,54,65,76,87,98], start_delay=6400, interval=100)
        self.set_mesh(trigger_ids=[2,13,24,35,46,57,68,79,90], start_delay=7200, interval=100)
        self.set_mesh(trigger_ids=[11,22,33,44,55,66,77,88,99], start_delay=8100, interval=100)


class 퍼즐패턴44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[9,8,7,6,5,4,3,2,1], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[20,30,40,50,60,70,80,90,100], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[91], start_delay=1900)
        self.set_mesh(trigger_ids=[81,71,61,51,41,31,21,11], start_delay=2000, interval=100)
        self.set_mesh(trigger_ids=[92,93,94,95,96,97,98,99], start_delay=2800, interval=100)
        self.set_mesh(trigger_ids=[19], start_delay=3600)
        self.set_mesh(trigger_ids=[18,17,16,15,14,13,12], start_delay=3700, interval=100)
        self.set_mesh(trigger_ids=[29,39,49,59,69,79,89], start_delay=4400, interval=100)
        self.set_mesh(trigger_ids=[82], start_delay=5100)
        self.set_mesh(trigger_ids=[72,62,52,42,32,22], start_delay=5200, interval=100)
        self.set_mesh(trigger_ids=[83,84,85,86,87,88], start_delay=5800, interval=100)
        self.set_mesh(trigger_ids=[28], start_delay=6400)
        self.set_mesh(trigger_ids=[27,26,25,24,23], start_delay=6500, interval=100)
        self.set_mesh(trigger_ids=[38,48,58,68,78], start_delay=7000, interval=100)
        self.set_mesh(trigger_ids=[73], start_delay=7500)
        self.set_mesh(trigger_ids=[63,53,43,33], start_delay=7600, interval=100)
        self.set_mesh(trigger_ids=[74,75,76,77], start_delay=8000, interval=100)
        self.set_mesh(trigger_ids=[37], start_delay=8400)
        self.set_mesh(trigger_ids=[36,35,34], start_delay=8500, interval=100)
        self.set_mesh(trigger_ids=[47,57,67], start_delay=8800, interval=100)
        self.set_mesh(trigger_ids=[64], start_delay=9100)
        self.set_mesh(trigger_ids=[54,44], start_delay=9200, interval=100)
        self.set_mesh(trigger_ids=[65,66], start_delay=9400, interval=100)


# 신규 추가 패턴
class 퍼즐패턴45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[34,33,23,24], interval=100)
        self.set_mesh(trigger_ids=[77,78,68,67], start_delay=400, interval=100)
        self.set_mesh(trigger_ids=[37,38,28,27], start_delay=800, interval=100)
        self.set_mesh(trigger_ids=[64,63,73,74], start_delay=1200, interval=100)
        self.set_mesh(trigger_ids=[55,45,46,56], start_delay=1600, interval=100)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10], start_delay=2000, interval=100)
        self.set_mesh(trigger_ids=[20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11], start_delay=3000, interval=100)
        self.set_mesh(trigger_ids=[12,13,14,15,16,17,18,19], start_delay=5600, interval=100)
        self.set_mesh(trigger_ids=[29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22], start_delay=6400, interval=100)


class 퍼즐패턴46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[33,23,24,34], interval=100)
        self.set_mesh(trigger_ids=[44,43,42,32,22,12,13,14,15,25,35,45], start_delay=400, interval=100)
        self.set_mesh(trigger_ids=[67,77,78,68,58,57,56,66,76,86,87,88,89,79,69,59], start_delay=1600, interval=100)
        self.set_mesh(trigger_ids=[37,38,28,27,26,36,46,47,48,49,39,29,19,18,17,16], start_delay=3200, interval=100)
        self.set_mesh(trigger_ids=[64,63,73,74,75,65,55,54,53,52,62,72,82,83,84,85], start_delay=4800, interval=100)


class 퍼즐패턴47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[33,23,24,34], interval=100)
        self.set_mesh(trigger_ids=[44,43,42,32,22,12,13,14,15,25,35,45], start_delay=400, interval=100)
        self.set_mesh(trigger_ids=[55,54,53,52,51,41,31,21,11,1,2,3,4,5,6,16,26,36,46,56], start_delay=1600, interval=100)
        self.set_mesh(trigger_ids=[61,71,81,91,92,93,94,95,96,97,98,99,100], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[90,80,70,60,50,40,30,20,10,9,8,7], start_delay=4900, interval=100)
        self.set_mesh(trigger_ids=[17,27,37,47,57,67,77,87,88,89,79,69,59,49,39,29,19,18,28,38,48,58,68,78,88], start_delay=6100, interval=100)


class 퍼즐패턴48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[33,23,24,34], interval=100)
        self.set_mesh(trigger_ids=[44,43,42,32,22,12,13,14,15,25,35,45], start_delay=400, interval=100)
        self.set_mesh(trigger_ids=[55,54,53,52,51,41,31,21,11,1,2,3,4,5,6,16,26,36,46,56], start_delay=1600, interval=100)
        self.set_mesh(trigger_ids=[61,71,81,91,92,93,94,95,96,97,98,99,100], start_delay=3600, interval=100)
        self.set_mesh(trigger_ids=[90,80,70,60,50,40,30,20,10], start_delay=4900, interval=100)
        self.set_mesh(trigger_ids=[9,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,73,74,75,76,77,78,68,67,66,65,64,63,62], start_delay=5800, interval=100)


class 퍼즐패턴49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[34,33,23,24], interval=100)
        self.set_mesh(trigger_ids=[77,78,68,67], start_delay=400, interval=100)
        self.set_mesh(trigger_ids=[45,44,43,42,32,22,12,13,14,15,25,35,56,57,58,59,69,79,89,88,87,86,76,66], start_delay=800, interval=100)
        self.set_mesh(trigger_ids=[55,54,53,52,51,41,31,21,11,1,2,3,4,5,6,16,26,36,46,47,48,49,50,60,70,80,90,100,99,98,97,96,95,85,75,65], start_delay=3200, interval=100)
        self.set_mesh(trigger_ids=[64], start_delay=7000, interval=100)
        self.set_mesh(trigger_ids=[37], start_delay=7000, interval=100)
        self.set_mesh(trigger_ids=[63,62,61], start_delay=7500, interval=100)
        self.set_mesh(trigger_ids=[74,84,94], start_delay=7500, interval=100)
        self.set_mesh(trigger_ids=[27,17,7], start_delay=7500, interval=100)
        self.set_mesh(trigger_ids=[38,39,40], start_delay=7500, interval=100)
        self.set_mesh(trigger_ids=[28], start_delay=7700, interval=100)
        self.set_mesh(trigger_ids=[73], start_delay=7700, interval=100)
        self.set_mesh(trigger_ids=[18,8], start_delay=8200, interval=100)
        self.set_mesh(trigger_ids=[29,30], start_delay=8200, interval=100)
        self.set_mesh(trigger_ids=[72,71], start_delay=8200, interval=100)
        self.set_mesh(trigger_ids=[83,93], start_delay=8200, interval=100)


class 퍼즐패턴50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[34,33,23,24], interval=100)
        self.set_mesh(trigger_ids=[77,78,68,67], start_delay=400, interval=100)
        self.set_mesh(trigger_ids=[37,38,28,27,64,63,73,74], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[82,81,91,92,19,20,10,9], start_delay=2100, interval=100)
        self.set_mesh(trigger_ids=[12,11,1,2,89,90,99,100], start_delay=3200, interval=100)
        self.set_mesh(trigger_ids=[15,5,6,16,86,96,85,95], start_delay=4300, interval=100)
        self.set_mesh(trigger_ids=[42,41,51,52,59,60,50,49], start_delay=5400, interval=100)
        self.set_mesh(trigger_ids=[55,45,46,56], start_delay=6500, interval=100)


class 퍼즐패턴51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[34,33,23,24], interval=100)
        self.set_mesh(trigger_ids=[77,78,68,67], start_delay=400, interval=100)
        self.set_mesh(trigger_ids=[37,38,28,27,64,63,73,74], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[82,83,93,92,91,81,71,72,19,18,8,9,10,20,30,29], start_delay=2100, interval=100)
        self.set_mesh(trigger_ids=[12,22,21,11,1,2,3,13,89,79,80,90,100,99,98,88], start_delay=3700, interval=100)
        self.set_mesh(trigger_ids=[15,5,6,16,86,96,85,95], start_delay=5300, interval=100)
        self.set_mesh(trigger_ids=[42,41,51,52,59,60,50,49], start_delay=6400, interval=100)
        self.set_mesh(trigger_ids=[55,45,46,56], start_delay=7500, interval=100)
        self.set_mesh(trigger_ids=[66,65,54,44,35,36,47,57], start_delay=8100, interval=100)


class 퍼즐패턴52(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1], interval=100)
        self.set_mesh(trigger_ids=[13,12,2,3], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[15,16,26,25,24,14,4,5,6], start_delay=500, interval=100)
        self.set_mesh(trigger_ids=[18,19,29,28,27,17,7,8,9,10,20,30,40,39,38,37], start_delay=1400, interval=100)
        self.set_mesh(trigger_ids=[68,58,59,69,79,78,77,67,57,47,48,49,50,60,70,80,90,89,88,87,86,76,66,56,46], start_delay=3000, interval=100)
        self.set_mesh(trigger_ids=[73,74,84,83,82,72,62,63,64,65,75,85,95,94,93,92], start_delay=5500, interval=100)
        self.set_mesh(trigger_ids=[42,43,53,52,51,41,31,32,33], start_delay=7100, interval=100)
        self.set_mesh(trigger_ids=[44,34,35,45], start_delay=8000, interval=100)
        self.set_mesh(trigger_ids=[55], start_delay=8400, interval=100)


class 퍼즐패턴53(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1], interval=100)
        self.set_mesh(trigger_ids=[13,12,2,3], start_delay=100, interval=100)
        self.set_mesh(trigger_ids=[15,16,26,25,24,14,4,5,6], start_delay=500, interval=100)
        self.set_mesh(trigger_ids=[18,19,29,28,27,17,7,8,9,10,20,30,40,39,38,37], start_delay=1400, interval=100)
        self.set_mesh(trigger_ids=[68,58,59,69,79,78,77,67,57,47,48,49,50,60,70,80,90,89,88,87,86,76,66,56,46], start_delay=3000, interval=100)
        self.set_mesh(trigger_ids=[96], start_delay=5500, interval=100)
        self.set_mesh(trigger_ids=[95,94,84,85], start_delay=5600, interval=100)
        self.set_mesh(trigger_ids=[82,83,93,92,91,81,71,72,73], start_delay=6000, interval=100)
        self.set_mesh(trigger_ids=[52,42,43,53,63,62,61,51,41,31,32,33,34,44,54,64], start_delay=6900, interval=100)


class 퍼즐패턴54(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,100], interval=100)
        self.set_mesh(trigger_ids=[13,12,2,3,88,89,99,98], start_delay=200, interval=100)
        self.set_mesh(trigger_ids=[15,16,26,25,24,14,4,5,6,86,85,75,76,77,87,97,96,95], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[18,19,29,28,27,17,7,8,9,10,20,30,40,39,38,37,83,82,72,73,74,84,94,93,92,91,81,71,61,62,63,64], start_delay=2800, interval=100)
        self.set_mesh(trigger_ids=[50,51], start_delay=6000, interval=100)
        self.set_mesh(trigger_ids=[60,70,69,59,41,31,32,42], start_delay=6200, interval=100)
        self.set_mesh(trigger_ids=[57,58,68,67,66,56,46,47,48,44,43,33,34,35,45,55,54,53], start_delay=7000, interval=100)


class 퍼즐패턴55(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,100], interval=100)
        self.set_mesh(trigger_ids=[13,12,2,3,88,89,99,98], start_delay=200, interval=100)
        self.set_mesh(trigger_ids=[15,16,26,25,24,14,4,5,6,86,85,75,76,77,87,97,96,95], start_delay=1000, interval=100)
        self.set_mesh(trigger_ids=[18,19,29,28,27,17,7,8,9,10,20,30,40,39,38,37,83,82,72,73,74,84,94,93,92,91,81,71,61,62,63,64], start_delay=2800, interval=100)
        self.set_mesh(trigger_ids=[59,60,70,69,68,58,48,49,50,42,41,31,32,33,43,53,52,51], start_delay=6000, interval=100)
        self.set_mesh(trigger_ids=[56,57,67,66,45,44,34,35], start_delay=7800, interval=100)
        self.set_mesh(trigger_ids=[46,55], start_delay=8600, interval=100)


class 퍼즐패턴56(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,19,29,69,79,89,88,87,84,83,82,72,62,22,25,26,38,48,58,78,76,75,73,53,43,33,34,37,47,57,67,66,65,64,54,44,45,46,56,55], interval=100)


class 퍼즐패턴57(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,8,9,10,20,30,40,50,90,100,99,92,91,81,41,31,21,11,12,13,14,17,18,19,29,39,59,69,79,88,87,86,85,84,83,72,62,52,32,22,23,26,27,28,48,58,68,78,77,74,73,63,53,43,34,35,47,67,66,65,64,44,45,46,56,55], interval=100)


class 퍼즐패턴58(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,29,39,49,59,69,79,89,88,87,86,85,84,83,72,62,52,42,32,22,23,25,26,48,58,78,77,76,75,53,43,33,34,37,67,66,64,44,46,55], interval=100)


class 퍼즐패턴59(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[1,2,6,7,8,9,10,20,30,40,50,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,13,14,15,17,18,19,29,39,59,69,79,78,77,76,75,74,73,23,24,25,27,28,38,58,68,67,66,65,64,63,53,43,33,34,35,37,57,67,66,65,64,54,44,45,56,55], interval=100)


class 퍼즐패턴60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[10])
        self.set_mesh(trigger_ids=[9,20], start_delay=500)
        self.set_mesh(trigger_ids=[8,19,30], start_delay=1000)
        self.set_mesh(trigger_ids=[7,18,29,40], start_delay=1500)
        self.set_mesh(trigger_ids=[28,39,50], start_delay=2000)
        self.set_mesh(trigger_ids=[5,16,49,60], start_delay=2500)
        self.set_mesh(trigger_ids=[4,15,26,37,59,70], start_delay=3000)
        self.set_mesh(trigger_ids=[3,14,25,47,69,80], start_delay=3500)
        self.set_mesh(trigger_ids=[2,13,24,46,57,90], start_delay=4000)
        self.set_mesh(trigger_ids=[1,12,23,34,45,56,78,100], start_delay=4500)
        self.set_mesh(trigger_ids=[11,22,55,66,77,88,99], start_delay=4000)
        self.set_mesh(trigger_ids=[21,43,65,87], start_delay=3500)
        self.set_mesh(trigger_ids=[31,42,53,64,75], start_delay=3000)
        self.set_mesh(trigger_ids=[52,74,85,96], start_delay=2500)
        self.set_mesh(trigger_ids=[73,84,95], start_delay=2000)
        self.set_mesh(trigger_ids=[61,72,83,94], start_delay=1500)
        self.set_mesh(trigger_ids=[71,82,93], start_delay=1000)
        self.set_mesh(trigger_ids=[81,92], start_delay=500)
        self.set_mesh(trigger_ids=[91])


initial_state = 재생버튼
