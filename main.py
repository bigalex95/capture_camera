import cv2
import yaml

with open(r'./conf.yaml') as file:
    conf = yaml.load(file, Loader=yaml.FullLoader)

cap = cv2.VideoCapture(conf["src"])

cv2.namedWindow('Preview', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Preview', conf["preview_width"], conf["preview_height"])

index = 0

try:
    while True:
        _, frame = cap.read()
        cv2.imshow("Preview", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break
        elif key == ord('s'):
            print("save")
            cv2.imwrite(str(index) + conf["name"] + conf["format"], frame)
            index += 1
        elif key == ord('S'):
            cv2.imwrite(str(index) + conf["name"] + conf["format"], frame)
            index += 1
except Exception as e:
    print(e)
    cv2.destroyAllWindows()
    cap.release()
