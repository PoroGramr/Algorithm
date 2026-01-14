import java.io.*;

public class Main {

    static class Node {
        char data;
        Node prev, next;

        Node(char data) {
            this.data = data;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String init = br.readLine();
        int M = Integer.parseInt(br.readLine());

        // 더미 노드 (head, tail)
        Node head = new Node('\0');
        Node tail = new Node('\0');
        head.next = tail;
        tail.prev = head;

        // 초기 문자열 연결 리스트 구성
        Node cursor = head;
        for (char c : init.toCharArray()) {
            Node newNode = new Node(c);
            insert(cursor, newNode);
            cursor = newNode;
        }

        for (int i = 0; i < M; i++) {
            String cmd = br.readLine();
            char op = cmd.charAt(0);

            if (op == 'L') {
                if (cursor != head) cursor = cursor.prev;
            } 
            else if (op == 'D') {
                if (cursor.next != tail) cursor = cursor.next;
            } 
            else if (op == 'B') {
                if (cursor != head) {
                    Node toDelete = cursor;
                    cursor = cursor.prev;
                    delete(toDelete);
                }
            } 
            else if (op == 'P') {
                char x = cmd.charAt(2);
                Node newNode = new Node(x);
                insert(cursor, newNode);
                cursor = newNode;
            }
        }

        // 출력
        StringBuilder sb = new StringBuilder();
        Node cur = head.next;
        while (cur != tail) {
            sb.append(cur.data);
            cur = cur.next;
        }
        System.out.println(sb);
    }

    // cursor 뒤에 node 삽입
    static void insert(Node cursor, Node node) {
        node.prev = cursor;
        node.next = cursor.next;
        cursor.next.prev = node;
        cursor.next = node;
    }

    // node 삭제
    static void delete(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}
