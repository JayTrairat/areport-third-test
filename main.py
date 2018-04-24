# --*-- coding: utf-8 --*--
import re

def main():
    stop_words = [
        "ต่อ", "และ", "ตาม", "จำแนก",
        "-", "จาก", "ถึง", "ที่", "มี",
        "ราย", "การ", "จำนวน", "ทั่ว",
        "ของ", "ข้อมูล", "จปฐ", "บาท",
        "ราย", "อยู่", "โดย", "เป็น",
        "ใน", "ทั้งสิ้น", "สำเร็จ", "อื่นๆ",
        "ได้รับ", "สะสม", "สังกัด", "เฉพาะ",
        "แห่ง", "เดือน", "ๆ", "หรือ", "กทม.",
        "ช่วง", "ป.", "ท", ".", "แบบ", "ช่วง",
        "พ.ศ.", "พ", "ศ", "ป.ป.ช.", "ฯ", "รอบ",
        "ปี", "ราชอาณาจักร", "(", ")", "ครัวเรือน",
        "มาก", "น้อย",
        "จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์",
        "จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา.",
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
        "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม",
        "ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.",
        "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค.", "ณ", " ", ""
    ]
    with open('assets/original/original.txt', 'r', encoding='utf8') as source:
        contents = [content.strip() for content in source.readlines()]
        contents = [content.split('|') for content in contents]
        contents = [list(filter(lambda x : x not in stop_words and re.match('^\D+', x), content)) for content in contents]

    with open('assets/original/original_with_out_stop_word.txt', 'w', encoding='utf8') as outp:
        contents_with_out_stop_words = ['|'.join(content) for content in contents]
        outp.write('\n'.join(contents_with_out_stop_words))

    with open('assets/important_words_PRE.txt', 'w', encoding='utf8') as outp:
        PRE = [content[0] for content in contents]
        outp.write('\n'.join(PRE))
    with open('assets/important_words_MIDPRE.txt', 'w', encoding='utf8') as outp:
        MIDPRE = ['|'.join(content[1:-1]) for content in contents]
        outp.write('\n'.join(MIDPRE))
    with open('assets/important_words_POST.txt', 'w', encoding='utf8') as outp:
        POST = [content[len(content)-1] for content in contents]
        outp.write('\n'.join(POST))

if __name__ == '__main__':
    main()
