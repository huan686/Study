# 面向对象示例：学生成绩教务管理系统
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名：{self.name} | 语文成绩：{self.chinese} | 数学成绩：{self.math} | 英语成绩：{self.english} | 总分：{self.chinese+self.math+self.english}"

    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class Edumanagement:
    version = 1.0
    def __init__(self):
        self.student_list = []

    def add_student(self,):
        name = input("请输入要添加的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在，请重新输入！")
                return

        chinese = int(input("请输入学生的语文成绩："))
        math = int(input("请输入学生的数学成绩："))
        english = int(input("请输入学生的英语成绩："))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功！")
        else:
            print("学生各科成绩必须在0-100之间！！！")

    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")
                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("学生信息修改成功！")
                    print(f"修改后的成绩：{s}")
                    return
                else:
                    print("学生各科成绩必须在0-100之间！！！")
                    return
        print("未找到该学生，请重新输入！！！")

    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功！")
                return
        print("未找到该学生，请重新输入！！！")

    def show_student(self):
        name = input("请输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print("未找到该学生，请重新输入！！！")

    def show_students(self):
        for s in self.student_list:
            print(f"所有学生信息如下：\n{s}")

    def run_edumanagement(self):
        print(f"欢迎使用学生信息管理系统V{Edumanagement.version}")
        print("具体操作如下：")
        print()
        print("#####################################################################")
        print()
        print("#  1.添加学生  2.修改学生  3.删除学生  4.查询学生  5.查询所有学生  6.退出系统  #")
        print()
        print("#####################################################################")
        while True:
            choice = int(input("请输入要进行的操作（1-6）："))
            match choice:
                case 1:
                    self.add_student()
                case 2:
                    self.update_student()
                case 3:
                    self.delete_student()
                case 4:
                    self.show_student()
                case 5:
                    self.show_students()
                case 6:
                    print("祝您生活愉快！再见！")
                    break
                case _:
                    print("请输入合法操作！！！")


if __name__ == '__main__':
    try:
        edu = Edumanagement()
        edu.run_edumanagement()
    except Exception as e:
        print(e)