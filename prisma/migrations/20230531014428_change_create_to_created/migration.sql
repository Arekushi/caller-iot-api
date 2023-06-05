/*
  Warnings:

  - You are about to drop the column `create_at` on the `attendance` table. All the data in the column will be lost.
  - You are about to drop the column `create_at` on the `student` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "attendance" DROP COLUMN "create_at",
ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- AlterTable
ALTER TABLE "student" DROP COLUMN "create_at",
ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
